#!/bin/bash

for i in ${{inputs}}; do echo "  $i: ${!i}" >> ./secrets.yaml ; done
