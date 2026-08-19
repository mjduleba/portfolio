# Production-ready + AWS deployment plan (single EC2, cheapest/simplest path)

## Context

The portfolio repo (Django + DRF backend, Next.js frontend, Postgres) currently only has a dev-mode Docker setup: `manage.py runserver`, `npm run dev`, bind-mounted source, no static-file handling, no production security settings. Goal: deploy on AWS using the cheapest/simplest architecture — a single EC2 instance running Docker Compose, no custom domain yet — rather than App Runner or ECS Fargate.

This plan is broken into independent, PR-sized deliverables so each can be its own branch/PR rather than one large change.

Note: all DRF viewsets are already `ReadOnlyModelViewSet` (no public write surface via the API).  The GitHub repo (`mjduleba/portfolio`) is public, so the EC2 box can `git clone` it with no credentials.

## Deliverables

### 0. `docs: add deployment plan`
- This file. Merge first as a durable checklist for the rest of the work.

### 1. `feat(backend): production settings` — settings.py hardening + health check
- `backend/requirements.txt`: add `whitenoise`.
- `backend/portfolio/settings.py`:
  - `STATIC_ROOT = BASE_DIR / 'staticfiles'`; insert `WhiteNoiseMiddleware` right after `SecurityMiddleware`; compressed-manifest static storage — serves Django admin CSS/JS with no separate static server.
  - Env-gated hardening, defaulting `False` so the no-TLS launch isn't broken: `SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`, `SECURE_HSTS_SECONDS` (all via `config(..., default=False, cast=bool)`).
  - Minimal console `LOGGING` config (Django doesn't log to stdout by default outside `DEBUG`).
- `backend/core/`: add a trivial health-check view at `/api/health/` returning `{"status": "ok"}`, wired into `portfolio/urls.py`. This is what verifies every later deploy.
- Testable standalone: `python manage.py runserver` locally, hit `/api/health/`, confirm `/admin/` still renders (whitenoise doesn't break dev).

### 2. `feat(backend): production Docker image`
- `backend/Dockerfile`: replace the `runserver` CMD with `collectstatic --noinput && migrate && seed_all && gunicorn portfolio.wsgi:application --bind 0.0.0.0:8000 --workers 3` (gunicorn is already a dependency, just unused today).
- `backend/.dockerignore` (new): `venv`, `__pycache__`, `*.pyc`, `.git`, `staticfiles`.
- Testable standalone: `docker build` the image, run it with a local Postgres, confirm gunicorn serves `/api/health/` and `/admin/` static assets load.
- Depends on deliverable 1 (needs `collectstatic`/whitenoise in place).

### 3. `feat(frontend): production Docker image`
- `frontend/next.config.ts`: add `output: "standalone"` — trimmed production server bundle, no full `node_modules` needed in the final image.
- `frontend/Dockerfile`: convert to multi-stage (deps → build → runtime). Key gotcha: `NEXT_PUBLIC_API_URL` is inlined into the JS bundle at **build time**, not read at container start — must be a Docker build `ARG`/`ENV` in the build stage, not a runtime `environment:` var (the current dev compose relies on the latter, which won't work for a prod image). Runtime stage runs `node server.js` as a non-root user on port 3000.
- `frontend/.dockerignore` (new): `node_modules`, `.next`, `.git`.
- Testable standalone: `docker build --build-arg NEXT_PUBLIC_API_URL=http://localhost/api`, run the image, confirm it serves the built app on port 3000.
- Independent of deliverables 1-2, can be built in parallel.

### 4. `feat(deploy): production compose + nginx reverse proxy`
- `docker-compose.prod.yml` (new, alongside the existing dev `docker-compose.yml`): no bind mounts, no `db` service (Postgres moves to RDS in deliverable 6).
  - `backend` — builds from `backend/Dockerfile`, `env_file: .env`, `restart: unless-stopped`, not publicly published (only reachable via nginx).
  - `frontend` — builds with `NEXT_PUBLIC_API_URL` passed via `args:` (the public-facing URL, e.g. `http://<elastic-ip>/api` — not the internal `http://backend:8000` the dev compose uses), `restart: unless-stopped`.
  - `nginx` — `nginx:alpine`, mounts `deploy/nginx.conf`, publishes `80:80`, single public entry point.
- `deploy/nginx.conf` (new): `/api/`, `/admin/`, `/static/` → `backend:8000`; everything else → `frontend:3000`. Standard `X-Forwarded-For`/`X-Forwarded-Proto` headers.
- `.env.example` (new, repo root): placeholder values for every var the README documents, plus the three new `SECURE_*` flags (defaulted off).
- Testable standalone: `docker compose -f docker-compose.prod.yml up -d --build` against a local/temporary Postgres, confirm nginx correctly proxies both `/api/` and the frontend end-to-end from a browser.
- Depends on deliverables 1-3.

### 5. `docs: AWS deployment runbook`
- `deploy/setup-ec2.sh` (new): one-shot bootstrap script for a fresh EC2 box — installs Docker + the Compose plugin, enables the docker service, adds `ec2-user` to the docker group.
- `README.md`: add a "Deployment (AWS)" section with the concrete runbook:
  1. **RDS** — PostgreSQL `db.t3.micro` (free-tier eligible), 20GB gp3, single-AZ, default VPC, not publicly accessible; security group allows inbound 5432 only from the EC2 instance's security group.
  2. **EC2** — `t3.micro` Amazon Linux 2023 (free-tier eligible for 12 months on an eligible account), default VPC/subnet; security group allows inbound 22 from the user's IP only and inbound 80 from anywhere; allocate + associate an Elastic IP for a stable address.
  3. **Bootstrap** — SSH in, run `deploy/setup-ec2.sh`.
  4. **First deploy** — `git clone` the public repo, hand-write `.env` on the box (fresh `SECRET_KEY`; `ALLOWED_HOSTS`/`CORS_ALLOWED_ORIGINS` set to the Elastic IP; `DATABASE_URL` pointing at the RDS endpoint; `NEXT_PUBLIC_API_URL=http://<elastic-ip>/api`), then `docker compose -f docker-compose.prod.yml up -d --build`.
  5. **Redeploys** — `git pull && docker compose -f docker-compose.prod.yml up -d --build`. Noted as a natural candidate for a later GitHub Actions job, not built now.
  6. **TLS deferred** — no domain yet, so launch is plain HTTP on the Elastic IP. Follow-up once a domain exists: point it at the EIP, add Certbot for a free Let's Encrypt cert, flip the three `SECURE_*` env flags to `True`, add a 443 listener to `nginx.conf`.
- This deliverable is documentation + a shell script; the actual AWS console provisioning and first deploy is a manual operational step that happens *after* this PR merges, following the runbook it adds.

### 6. Execute the runbook (not a PR — operational)
- Actually provision RDS + EC2 per deliverable 5's steps and run the first deploy. Requires AWS console access; happens after deliverables 1-5 are merged.

## Explicitly out of scope for this pass

CI/CD, TLS/HTTPS, Terraform/IaC, load balancer/auto-scaling/multi-AZ, CloudWatch alarms — flagged as future follow-ups, not built now.

## Verification

- Each deliverable above has its own standalone test noted inline — verify it before merging that PR.
- After deliverable 4: full local prod-mode run via `docker-compose.prod.yml`.
- After deliverable 6 (live on EC2): load `http://<elastic-ip>/` (frontend renders, fetches real data) and `http://<elastic-ip>/admin/` (styled login page, static assets load) from a browser; confirm RDS's security group rejects connections from outside the EC2 security group (e.g. `psql` from a laptop should time out).
