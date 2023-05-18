#!/bin/bash

echo "# Commit Timestamps" > README.md
git log --format="%ai %h" --name-only | awk '
  {
    if ($1 ~ /^[0-9]{4}-[0-9]{2}-[0-9]{2}$/) {
      date = $0;
    } else if ($1 ~ /^[0-9]{2}:[0-9]{2}:[0-9]{2}$/) {
      time = $0;
    } else if ($1 != "") {
      printf("- %s %s %s\n", date, time, $0);
    }
  }' | sort | uniq >> README.md
