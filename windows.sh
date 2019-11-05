#!/usr/bin/env bash
set -e

pip install virtualenv
pip install jupyterlab
virtualenv -p python venv
source venv/Scripts/activate
pip install -r requirements.txt
python -m ipykernel install --user --name=explainator-py