#!/bin/bash
first_args=$1

echo "You first variable is $first_args"


echo "All numbers from 0 to first_args - 1:"
for ((i=0;i<$first_args;i++)); do
    echo $i
done