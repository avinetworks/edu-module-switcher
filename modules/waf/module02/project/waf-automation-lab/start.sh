#!/bin/sh

echo "AVI_USERNAME: $AVI_USERNAME"
echo "AVI_PASSWORD: $AVI_PASSWORD"
echo "AVI_CONTROLLER: $AVI_CONTROLLER"
jupyter notebook iWAF-Demo-notebook.ipynb --config=./jupyter_notebook_config.py --allow-root

