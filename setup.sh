#!/bin/bash
apt-get update
apt-get install -y gcc python3-dev build-essential
pip install --upgrade pip
pip install setuptools wheel cython numpy
python setup.py build_ext --inplace