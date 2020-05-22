#!/bin/bash

for (( i = 30; i <= 5000; i+=1000 ))
do
  let "count_edges = i * 10"
  python3 generation.py -e $count_edges -v $i -g 'best for ford-bellman' -s 0 -f best$i.txt
  python3 generation.py -e $count_edges -v $i -g 'connected random graph' -s 0 -f random$i.txt
  python3 generation.py -e $count_edges -v $i -g 'worst for ford-bellman' -s 0 -f worst$i.txt
done

