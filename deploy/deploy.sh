#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="/home/widson/Projetos/Nexus"
VENV_DIR="$REPO_DIR/.venv"
APP_SERVICE="nexus"

export FLASK_APP=wsgi.py
export PYTHONUNBUFFERED=1

cd "$REPO_DIR"

# atualiza código
git fetch origin main
if ! git rev-parse --abbrev-ref --symbolic-full-name @{u} >/dev/null 2>&1; then
  git branch --set-upstream-to=origin/main main || true
fi

git reset --hard
git clean -fd
git checkout main
git pull --rebase origin main

# venv + deps
if [ ! -d "$VENV_DIR" ]; then
  python3 -m venv "$VENV_DIR"
fi
source "$VENV_DIR/bin/activate"
pip install --upgrade pip
pip install -r requirements.txt

# migrações
flask db upgrade

# restart serviço
sudo systemctl restart "$APP_SERVICE"
systemctl status "$APP_SERVICE" --no-pager -l | sed -n '1,20p'
echo "Deploy OK."
