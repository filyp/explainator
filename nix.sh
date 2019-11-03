#!/usr/bin/env bash
pip install virtualenv
pip install jupyterlab
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name=explainator-py
