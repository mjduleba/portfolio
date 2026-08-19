#!/usr/bin/env bash
# One-shot bootstrap for a fresh Compute Engine VM (Debian 12 default image).
# Installs Docker + the Compose plugin and enables the current user to run
# docker commands without sudo. Run once via SSH after first boot:
#
#   gcloud compute ssh <instance-name> --zone <zone>
#   curl -fsSL https://raw.githubusercontent.com/mjduleba/portfolio/main/deploy/setup-gce.sh | bash
#
# or copy the script over and run it directly.

set -euo pipefail

curl -fsSL https://get.docker.com | sh

sudo systemctl enable --now docker
sudo usermod -aG docker "$USER"

echo "Docker + Compose installed. Log out and back in (or run 'newgrp docker')"
echo "for the docker group membership to take effect, then verify with:"
echo "  docker compose version"
