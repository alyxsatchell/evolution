#!bin/sh
set -eu

export FLASK_RUN_HOST=0.0.0.0
python3 webGraphics.py &
python3 evolution.py

