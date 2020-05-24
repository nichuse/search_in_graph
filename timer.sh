#!/bin/bash

cd 'generated_graphs' || exit
names=$(ls)
cd .. || exit
for file in $names;
do
  python3 time_manager.py -a 'ford-bellman' -r $file -n 11 -w resultford-bellman$file
  python3 time_manager.py -a 'dijkstra' -r $file -n 11 -w resultdijkstra$file
  python3 time_manager.py -a 'levit' -r $file -n 11 -w resultlevit$file
  python3 time_manager.py -a 'other' -r $file -n 11 -w resultother$file
done
