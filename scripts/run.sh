#!/usr/bin/env sh
set -eu
PYTHONPATH=src exec python -m dip "$@"
