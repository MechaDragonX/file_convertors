#!/bin/bash

for i in */; do zip -0 -r "${i%/}.cbz" "$i" & done; wait
