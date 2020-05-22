#!/bin/bash

cd 'generated_graphs' || exit
names=$(ls)
cd .. || exit
for file in $names;
do
  python3 time_manager.py -a 'ford-bellman' -r $file -n 10 -w result$file
done
