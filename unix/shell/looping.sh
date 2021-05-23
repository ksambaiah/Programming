#!/bin/sh
# Example of for loop 
for i in a b xyz cd m i j f h 2 c
do
  echo "I am at the $i"
done

for i in `seq 5`
do
   echo "Value of i is $i"
done

for i in `seq 20 -4 0`
do
   echo "Value of i is $i"
done
