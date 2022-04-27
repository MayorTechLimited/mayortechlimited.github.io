#!/bin/bash
set -eu

. venv/bin/activate

rm -rf dist
staticjinja build --outpath ./dist

ghp-import dist --branch=main --cname=www.mayortech.co.uk
git push origin main:main
