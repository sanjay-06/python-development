#!/usr/bin/env bash

for file *.HTM; do
    name=$(basename "$file" .HTM)
    mv "$file" "$name.html"
done
