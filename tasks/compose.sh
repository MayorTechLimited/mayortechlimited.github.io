#!/bin/bash
# ---
# help-text: Run a compose command
# ---
set -eu

docker compose "${@:---help}"
