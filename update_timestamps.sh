#!/bin/bash

echo "# Commit Timestamps" > README.md

files=$(git log --format=format: --name-only | sort -u)

for file in $files
do
    echo "- File: $file" >> README.md
    git log --format="%ai %h" --follow -- $file | sort | uniq >> README.md
    echo "" >> README.md
done
