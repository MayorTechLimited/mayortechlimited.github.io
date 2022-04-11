#!/bin/bash

. venv/bin/activate

pelican content -o output -s publishconf.py

cd output
rm -rf author blog/ category/ feeds/ theme/ archives.html authors.html  categories.html  tags.html
cd -

ghp-import output -b main

git push origin main:main
