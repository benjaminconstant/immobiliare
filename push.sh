#!/bin/bash
set -e

ENV=t4_catalog

source $WORKON_HOME/$ENV/bin/activate
yarn install
quasar build
pip freeze -> django/requirements.txt
git add .
git commit -m "push"
git push origin master
