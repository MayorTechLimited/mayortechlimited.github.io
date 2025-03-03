#!/bin/bash
# ---
# help-text: Deploy the site
# environent:
#   - HOME
#   - USER
# ---
set -eu

rm -rf dist
vg compose run --remove-orphans css /tailwindcss -i ./styles.css -o ./dist/styles.css --minify
vg compose run --remove-orphans static /venv/bin/python watch_static.py --build
vg compose run --remove-orphans templates /venv/bin/python watch_templates.py --build

TMP=$(mktemp --directory)
cp -r dist/* "$TMP"/
git stash push --all
git checkout main

function cleanup() {
    rm -rf "$TMP"
    git checkout develop
    git stash pop
}
trap cleanup EXIT

rm -rf ./*
cp -r "$TMP"/* ./
echo 'www.mayortech.co.uk' > CNAME

D=$(date +"%Y-%m-%dT%H:%M:%S")
git commit -am "Deploy on $D"
git push origin main
