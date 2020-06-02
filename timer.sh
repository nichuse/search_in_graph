#!/bin/bash

cd 'generated_graphs' || exit
names=$(ls)
cd .. || exit

#current_date_time="`date "+%Y-%m-%d %H:%M:%S"`";
#
#echo $current_date_time;
#
#for file in $names;
#do
#  if grep -q "randomcomplete" <<< "$file"; then
#      echo
#  elif grep -q "random" <<< "$file"; then
#      python3 time_manager.py -a 'ford-bellman' -r $file -w result-ford-random -p /home/asd/PycharmProjects/search_in_graph/
#  elif grep -q "worstlevit" <<< "$file"; then
#      python3 time_manager.py -a 'ford-bellman' -r $file -w result-ford-worst-levit -p /home/asd/PycharmProjects/search_in_graph/
#  fi
#done
#
#current_date_time="`date "+%Y-%m-%d %H:%M:%S"`";
#echo $current_date_time;
#
#for file in $names;
#do
#  if grep -q "randomcomplete" <<< "$file"; then
#      python3 time_manager.py -a 'levit' -r $file -w result-levit-random-complete -p /home/asd/PycharmProjects/search_in_graph/
#  elif grep -q "random" <<< "$file"; then
#      python3 time_manager.py -a 'levit' -r $file -w result-levit-random -p /home/asd/PycharmProjects/search_in_graph/
#  fi
#done

current_date_time="`date "+%Y-%m-%d %H:%M:%S"`";
echo $current_date_time;

for file in $names;
do
  if grep -q "randomcomplete" <<< "$file"; then
      python3 time_manager.py -a 'other' -r $file -w result-other-random-complete -p /home/asd/PycharmProjects/search_in_graph/
  elif grep -q "worstlevit" <<< "$file"; then
      python3 time_manager.py -a 'other' -r $file -w result-other-worst-levit -p /home/asd/PycharmProjects/search_in_graph/
  fi
done

current_date_time="`date "+%Y-%m-%d %H:%M:%S"`";
echo $current_date_time;

for file in $names;
do
  if grep -q "random" <<< "$file"; then
      python3 time_manager.py -a 'other' -r $file -w result-other-random -p /home/asd/PycharmProjects/search_in_graph/
  elif grep -q "bestford" D<<< "$file"; then
      python3 time_manager.py -a 'other' -r $file -w result-other-best-ford -p /home/asd/PycharmProjects/search_in_graph/
  elif grep -q "worstford" <<< "$file"; then
      python3 time_manager.py -a 'other' -r $file -w result-other-worst-ford -p /home/asd/PycharmProjects/search_in_graph/
  fi
done