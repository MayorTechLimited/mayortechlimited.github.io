#!/bin/bash
# ---
# help-text: Run the debug servers
# environment:
#   - HOME
#   - USER
#   - TERM
# ---
set -eu

docker compose up css templates static serve
