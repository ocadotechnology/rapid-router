#!/bin/sh

find game/static/game/image -name "*.svg" ! -name "tile1.svg" ! -name "van_small*.svg" -print0 | xargs -0 perl -0pi -e 's/<svg([^<]*)width="([0-9\.]+)(?:px)?"[ \n]*height="([0-9\.]+)(?:px)?"(?:[ \n]*viewBox="0 0 [0-9\.]+ [0-9\.]+")?/<svg$1viewBox="0 0 $2 $3"/g;' -e 's/<svg([^<]*)x="0px"[ \n]*y="0px"/<svg$1/g;'

