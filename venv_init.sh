#!/bin/bash
echo venv_name
read venv_name
python3 -m venv $venv_name
source $venv_name/bin/activate
cp requirements.txt $venv_name/requirements.txt
cd $venv_name
pip3 install -r requriements.txt