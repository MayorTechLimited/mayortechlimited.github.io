#!/bin/bash
set -eu

. venv/bin/activate

rm -rf dist
staticjinja build --outpath ./dist
tailwindcss -i ./styles.css -o ./dist/styles.css --minify

ghp-import dist --branch=main --cname=www.mayortech.co.uk
git push origin main:main
