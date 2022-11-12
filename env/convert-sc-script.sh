#!/bin/bash
python -v
for i in $(declare -xp | grep --perl-regexp --only-match '(?<=^declare -x )[^=]+' | grep INPUT_); do echo "  $i: ${!i}" >> ./secrets.yaml ; done
