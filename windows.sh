#!/usr/bin/env bash
pip install virtualenv
pip install jupyterlab
virtualenv -p python venv
source venv/Scripts/activate
pip install -r requirements.txt
python -m ipykernel install --user --name=explainator-py