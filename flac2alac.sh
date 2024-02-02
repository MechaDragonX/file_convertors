#!/bin/bash

# Usage: ./flac2alac.sh <input directory without '/' at the end> <output dir w/o '/'>
# Example: ./flac2alac.sh "~/Music/Super Mario 64" ~/Downloads/apple_mario

mkdir -p $2

for file in $1/*; do
    if [ -d "$1" ]; then
        if [[ $file == *.flac ]] then
            filename_ext=$(basename "$file")
            filename="${filename_ext%.*}"
            ffmpeg -i "$file" -c:a alac -c:v copy "$2/${filename}.m4a"
        fi
    else
        echo "Not a directory!"
    fi
done
