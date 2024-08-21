#!/bin/bash -e

git submodule update --init
cd ti_lpc/cmd_line_vers && make && cd -
python3 generate.py
