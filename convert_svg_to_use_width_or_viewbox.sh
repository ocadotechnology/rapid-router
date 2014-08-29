#!/bin/sh

# The reason for all this is differences between how the browsers treat SVG files.
# - Raphael on Chrome needs them to have width, height, x, y.
# - IE not in Raphael needs them to use viewBox only. Hence, all of this!

# remove origin, remove width="100%, remove height="100%", convert to viewbox, remove double spaces
find game/static/game/image -name "*.svg" -print0 | xargs -0 perl -0pi -e 's/<svg([^<]*)x="0px"/<svg$1/g;' -e 's/<svg([^<]*)y="0px"/<svg$1/g;' -e 's/<svg([^<]*)width="100%"/<svg$1/g;' -e 's/<svg([^<]*)height="100%"/<svg$1/g;' -e 's/<svg([^<]*)width="([0-9\.]+)(?:px)?"[ \n]*height="([0-9\.]+)(?:px)?"(?:[ \n]*viewBox="0 0 [0-9\.]+ [0-9\.]+")?/<svg$1viewBox="0 0 $2 $3"/g;' -e 's/<svg([^<]*)height="([0-9\.]+)(?:px)?"(?:[ \n]*viewBox="0 0 [0-9\.]+ [0-9\.]+")[ \n]*width="([0-9\.]+)(?:px)?"/<svg$1viewBox="0 0 $3 $2"/g;' -e 's/ +/ /g;' 

# copy everything to a special directory for chrome
rsync -av --delete game/static/game/image/* game/static/game/chrome_image

# convert chrome images back to width/height
find game/static/game/chrome_image -name "*.svg" ! -name "tile1.svg" ! -name "van_small*.svg" -print0 | xargs -0 perl -0pi -e 's/<svg([^<]*)viewBox="0 0 ([0-9\.]+) ([0-9\.]+)"/<svg$1x="0px" y="0px" width="$2px" height="$3px"/g;'