#!/usr/bin/env python3
import sys
import argparse

""" This program opens file for reading, and do some thing and exits """

def openfile(filen):
    try:
        with open(filen, 'r') as f:
            data = f.read()
    except FileNotFoundError:
        print("File not found!")
        sys.exit(100)
    except IOError as e:
        print("An error occurred:", e)
        sys.exit(101)


def get_args():
    parser = argparse.ArgumentParser(prog='selectionsort.py', description='File need to be passed')
    parser.add_argument('-f', dest='filen', help='filename has to be provided', required=True)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
   args = get_args()
   openfile(args.filen)
   sys.exit(0) 
