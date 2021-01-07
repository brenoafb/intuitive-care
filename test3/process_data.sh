#!/usr/bin/env sh

mkdir -p processed-data

for i in data/*.csv
do
  f=`basename $i`
  echo "$f"
  if [[ "$OSTYPE" == "darwin"* ]]; then
    LANG=latin1 sed -e 's/,/./g' "$i" > "processed-data/$f"
  elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    LANG=latin1 sed -i 's/,/./g' "$i" > "processed-data/$f"
  fi
done
