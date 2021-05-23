#!/bin/sh
# Testing to loop over args

# This is always right

echo "using unquote $@"
for var in $@
do
    echo $var
done

echo "using quote $@"
for var in "$@"
do
    echo $var
done

echo "Using unquote $*"
for var in $*
do
    echo $var
done

echo "Using quote $*"
for var in "$*"
do
    echo $var
done
