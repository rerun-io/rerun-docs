set -eu

wl-paste > "$1"
convert "$1" \( +clone -background black -shadow 50x10+15+15  \) +swap -background none -layers merge +repage "$1"
