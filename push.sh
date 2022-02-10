#!/bin/bash
set -e

ENV=immobiliare

source $WORKON_HOME/$ENV/bin/activate
yarn install
quasar build
pip freeze -> django/requirements.txt
git add .
git commit -m "push"
git push origin master
