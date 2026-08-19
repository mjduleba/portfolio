# portfolio

My personal portfolio site — a content-driven monorepo pairing a Next.js frontend with a Django REST API backend. All page content (profile, skills, experience, projects, tools) lives in Postgres database and is served through the Django REST API.

## Tech stack

| Layer      | Technology                                      |
| ---------- | ------------------------------------------------ |
| Frontend   | Next.js 16 (App Router), React 19, TypeScript, Tailwind CSS 4 |
| Backend    | Django 5, Django REST Framework, django-cors-headers |
| Database   | PostgreSQL 16                                     |
| Tooling    | ESLint, Prettier, Docker Compose                  |

## Repository structure

```
portfolio/
├── backend/                    # Django REST API
│   ├── portfolio/              # Project settings, root URL conf
│   ├── core/                   # Shared app config, seed_all orchestrator command
│   ├── userprofile/            # Profile, hobbies, education
│   ├── skills/                 # Skills, grouped by category
│   ├── experience/             # Work experience + bullets
│   ├── projects/               # Portfolio projects + bullets
│   ├── tools/                  # Tools section: demos, guides, skill/agent entries
│   └── requirements.txt
├── frontend/                   # Next.js app
│   └── src/
│       ├── app/                # Routes (home page, /tools/[slug])
│       ├── components/
│       │   ├── layout/         # Header, page chrome
│       │   ├── sections/       # About, Skills, Experience, Projects, Tools, Guide
│       │   └── ui/             # Card, Modal, Tag, CodeBlock, etc.
│       └── lib/
│           ├── api/            # Typed fetch clients per resource
│           └── hooks/
├── docker-compose.yml          # backend + frontend + Postgres for local dev
```

## Architecture

The frontend is a server-rendered Next.js app. The home page (`frontend/src/app/page.tsx`) fetches all section data in parallel from the Django API at request time and renders it into the corresponding section components:

```
Next.js (page.tsx)
  ├─ getProfile()    → GET /api/profile/
  ├─ getSkills()     → GET /api/skills/
  ├─ getExperience() → GET /api/experience/
  ├─ getProjects()   → GET /api/projects/
  └─ getTools()      → GET /api/tools/
```

Each backend app owns one content domain (models, serializers, views, admin, seed command) and is wired into `portfolio/urls.py` under the `/api/` prefix via DRF `DefaultRouter`s.

## Getting started

### Option A — Docker Compose (recommended)

Brings up Postgres, the Django API, and the Next.js dev server together, with migrations and seed data applied automatically on backend startup.

```bash
docker compose up
```

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000/api/
- Django admin: http://localhost:8000/admin/

### Option B — Run services locally

**Backend**

```bash
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_all
python manage.py runserver
```

**Frontend**

```bash
cd frontend
npm install
npm run dev
```

### Environment variables

Create a `.env` file at the repo root (used by both `docker-compose.yml` and the Django app):

| Variable                | Description                                         |
| ------------------------ | ---------------------------------------------------- |
| `SECRET_KEY`              | Django secret key                                     |
| `DEBUG`                   | `True`/`False`                                        |
| `ALLOWED_HOSTS`            | Comma-separated hosts Django will serve                |
| `CORS_ALLOWED_ORIGINS`     | Comma-separated origins allowed to call the API         |
| `DATABASE_URL`             | Postgres connection string (used outside Docker)         |
| `POSTGRES_USER`            | Postgres username (Docker Compose `db` service)         |
| `POSTGRES_PASSWORD`        | Postgres password (Docker Compose `db` service)         |
| `POSTGRES_DB`               | Postgres database name (Docker Compose `db` service)      |
| `NEXT_PUBLIC_API_URL`      | Base URL the frontend uses to reach the API              |

See `.env.example` for a full template, including the production `SECURE_*` flags.

## Hosting

Deployed on **GCP Compute Engine** — a single `e2-micro` instance running the full stack via `docker-compose.prod.yml`:

```
Internet → nginx (:80)
             ├─ /api/, /admin/, /static/  → Django + gunicorn (:8000)
             └─ everything else           → Next.js standalone server (:3000)

PostgreSQL runs in its own container alongside the app.
```

- **Backend** — multi-stage Docker image; gunicorn serves the Django app, WhiteNoise serves static/admin assets, `/api/health/` is the deploy healthcheck.
- **Frontend** — multi-stage Docker image using Next.js `output: "standalone"` for a minimal production runtime; all data fetching happens server-side.
- **Reverse proxy** — nginx routes API/admin/static traffic to Django and everything else to the Next.js SSR app.
- **Database** — PostgreSQL, containerized on the same instance.

See the Dockerfiles and `docker-compose.prod.yml` for the full production configuration.

## Backend

Each Django app follows the same shape: `models.py`, `serializers.py`, `views.py` (DRF `ViewSet`), `urls.py`, `admin.py`, and a `management/commands/seed_*.py` command that seeds its own data.

| App          | Responsibility                                            | Endpoint         |
| ------------ | ----------------------------------------------------------- | ----------------- |
| `userprofile` | Profile, hobbies, education                                  | `/api/profile/`    |
| `skills`      | Skills grouped by category (Languages, Frameworks, Cloud, Concepts) | `/api/skills/`      |
| `experience`  | Work history with tagged bullet points                        | `/api/experience/`  |
| `projects`    | Portfolio projects with tagged bullet points                  | `/api/projects/`    |
| `tools`       | Tools section: demos, skill/agent write-ups, pattern guides    | `/api/tools/`        |
| `core`        | Shared app config; hosts the `seed_all` command that runs every app's seeder | —                |

Run `python manage.py seed_all` (or let the Docker `backend` container do it on startup) to reset all content to its seed state.

## Frontend

- **`app/`** — Next.js App Router routes: the single-page home (`page.tsx`) and dynamic tool detail pages (`tools/[slug]/page.tsx`).
- **`components/sections/`** — one component per home-page section (About, Tools, Skills, Experience, Projects), plus `GuideContent`/`SkillAgentsContent` for tool detail views.
- **`components/ui/`** — shared presentational primitives (Card, Modal, Tag, CodeBlock, IconRow, ToolCard).
- **`lib/api/`** — typed fetch clients, one per backend resource, all going through a shared `client.ts`.

## Scripts reference

| Command                          | Where       | Does                          |
| --------------------------------- | ------------ | ------------------------------ |
| `python manage.py runserver`        | `backend/`   | Start the Django dev server      |
| `python manage.py seed_all`         | `backend/`   | Seed all app content              |
| `python manage.py migrate`          | `backend/`   | Apply database migrations          |
| `npm run dev`                       | `frontend/`  | Start the Next.js dev server       |
| `npm run build` / `npm run start`   | `frontend/`  | Production build / serve           |
| `npm run lint`                      | `frontend/`  | ESLint                            |
| `npm run format`                    | `frontend/`  | Prettier write                     |
