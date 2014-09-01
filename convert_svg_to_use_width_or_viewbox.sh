#!/bin/bash

# The reason for all this is differences between how the browsers treat SVG files.
# The current state is:
# - on IE not in Raphael they need to use viewBox only.
# - on Chrome in Raphael they need to have width, height, x, y.
# - except for the tile1.svg files, which should use both
# - we also maybe want a set of images for mobile devices which would be less complicated
#       but keep the pretty images for use on desktops

# Therefore we've decided to have completely separate image directories for Raphael and not Raphael,
# this means there is some duplication but far less than if we'd had copies for each browser.
# It also makes it easy to have low quality versions alongside the pretty versions.

# First as a starting point, convert every image to just viewBox
# remove all of x=0", y="0", width="100%, height="100%", convert to viewbox, remove double spaces
find game/static/game/{image,raphael_image} -name "*.svg" -print0 | xargs -0 perl -0pi \
  -e 's/<svg([^<]*)x="0px"/<svg$1/g;' \
  -e 's/<svg([^<]*)y="0px"/<svg$1/g;' \
  -e 's/<svg([^<]*)width="100%"/<svg$1/g;' \
  -e 's/<svg([^<]*)height="100%"/<svg$1/g;' \
  -e 's/<svg([^<]*)width="([0-9\.]+)(?:px)?"[ \n]*height="([0-9\.]+)(?:px)?"(?:[ \n]*viewBox="0 0 [0-9\.]+ [0-9\.]+")?/<svg$1viewBox="0 0 $2 $3"/g;' \
  -e 's/<svg([^<]*)height="([0-9\.]+)(?:px)?"(?:[ \n]*viewBox="0 0 [0-9\.]+ [0-9\.]+")[ \n]*width="([0-9\.]+)(?:px)?"/<svg$1viewBox="0 0 $3 $2"/g;' \
  -e 's/ +/ /g;'

# convert all raphael images back to using width, height, x, y, and viewBox
find game/static/game/raphael_image -name "*.svg" -print0 | xargs -0 perl -0pi \
  -e 's/<svg([^<]*)viewBox="0 0 ([0-9\.]+) ([0-9\.]+)"/<svg$1x="0px" y="0px" width="$2px" height="$3px" viewBox="0 0 $2 $3"/g;'