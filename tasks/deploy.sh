#!/bin/bash
set -eu

. venv/bin/activate

rm -rf dist
staticjinja build --outpath ./dist
tailwindcss -i ./styles.css -o ./dist/styles.css --minify

ghp-import dist --branch=main --cname=www.mayortech.co.uk

git checkout main
git push origin main
git checkout develop
