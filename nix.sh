#!/usr/bin/env bash
set -e

pip install --user virtualenv
pip install --user jupyterlab
python3 -m venv .
source ./bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name=explainator-py
