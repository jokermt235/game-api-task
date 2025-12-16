#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset
set -e

echo "🔄 Running migrations..."
alembic upgrade head

export GUNICORN_CMD_ARGS="${GUNICORN_CMD_ARGS:-"-b 0.0.0.0:8000 --timeout 30 --graceful-timeout 30 --forwarded-allow-ips=* --max-requests=10000 --chdir=/app"}"

echo "Starting up Gunicorn server..."

exec gunicorn main:app -k uvicorn.workers.UvicornWorker
