#!/bin/bash

# Use this first argument to process only one directory,
# defaults to all images
DIR=../${1:-game/static/game/image}

cd scour
find $DIR -name "*.svg" -print0 > svgs.txt

cat svgs.txt | xargs -0 -I % python scour.py -i % -o %.opt
cat svgs.txt | xargs -0 -I % mv %.opt %

rm svgs.txt
