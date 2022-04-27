#!/bin/bash
set -eu

tailwindcss -i ./styles.css -o ./dist/styles.css --watch
