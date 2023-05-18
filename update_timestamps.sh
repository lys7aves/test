#!/bin/bash

echo "# Commit Timestamps" > README.md

git log --name-status --pretty=format:"%ai %h" | awk '
  /^commit/ {
    if (commit != "") {
      printf("- %s %s %s\n", date, time, file);
      file = "";
    }
    commit = $2;
  }
  /^Date:/ {
    date = $2;
    time = $3;
  }
  /^[A,C,D,M,R,T,U]/ {
    file = $2;
  }
  END {
    if (commit != "") {
      printf("- %s %s %s\n", date, time, file);
    }
  }
' | sort | uniq >> README.md
