#!/bin/bash

for (( i = 30; i <= 5030; i+=100 ))
do
  let "count_edges = i * 10"
  python3 generation.py -e $count_edges -v $i -g 'best for ford-bellman' -s 0 -f bestford$i.txt
  python3 generation.py -e $count_edges -v $i -g 'connected random graph' -s 0 -f random$i.txt
  python3 generation.py -e $count_edges -v $i -g 'worst for ford-bellman' -s 0 -f worstford$i.txt
done

for (( i = 30; i <= 2030; i+=100 ))
do
  let "count_edges = i * (i - 1)"
  python3 generation.py -e $count_edges -v $i -g 'connected random graph' -s 0 -f randomcomplete$i.txt
  python3 generation.py -e $count_edges -v $i -g 'worst for levit' -s 0 -f worstlevit$i.txt
done



