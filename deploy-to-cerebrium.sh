#!/bin/bash

# delete everything in dist
cd ./dist
rm -rf *
cd ..

# copy sources
cp ./cerebrium.toml ./dist/
cp ./requirements.txt ./dist/
cp ./src/main.py ./dist/

# create marimo script
marimo export script ./src/marimoapp.py -o ./dist/marimoapp_script.py

echo 
echo "dist updated."
echo 

# deploy
cd ./dist
cerebrium deploy