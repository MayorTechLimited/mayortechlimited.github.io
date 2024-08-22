#!/bin/bash
set -eu

. venv/bin/activate
python build.py --watch
