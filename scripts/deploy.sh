#!/bin/bash

. venv/bin/activate

rm -rf output
pelican content -o output -s publishconf.py

cd output
rm -rf author blog/ category/ feeds/ theme/ archives.html authors.html  categories.html  tags.html
cd -

ghp-import output --branch=main --cname=www.mayortech.co.uk

git push origin main:main
