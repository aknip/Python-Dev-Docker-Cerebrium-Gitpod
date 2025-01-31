#!/bin/bash

# deactivate current venv (if one is active)
if command -v deactivate &> /dev/null; then
    deactivate
fi

# remove .venv folder
rm -r .venv

uv venv
source .venv/bin/activate
uv pip install cerebrium

echo "Virtual environment activated, Cerebrium installed."