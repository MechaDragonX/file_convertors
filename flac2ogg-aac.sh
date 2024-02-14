#!/bin/bash

# Usage: ./flac2alac.sh <input directory without '/' at the end> <output dir w/o '/'>
# Example: ./flac2alac.sh "~/Music/Super Mario 64" ~/Downloads/apple_mario

if [[ $1 == *.flac ]] then
    filename_ext=$(basename "$1")
    filename="${filename_ext%.*}"
    ffmpeg -i "$1" -c:a libvorbis -c:a copy "${filename}.ogg"
    ffmpeg -i "$1" -c:a aac -c:v copy "${filename}.m4a"
else
    echo "Not a FLAC file!"
fi
