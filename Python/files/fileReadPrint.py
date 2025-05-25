#!/usr/bin/env python3
import sys
import argparse

""" This program opens file for reading, and do some thing and exits """

def openfile(filen):
    try:
        with open(filen, 'r') as f:
            for line in f:
               print(line.strip())
    except FileNotFoundError:
        print("File not found!")
    except IOError as e:
        print("An error occurred:", e)
    finally:
        if f:
           f.close()


def get_args():
    parser = argparse.ArgumentParser(prog='selectionsort.py', description='selection sort program sorts array of given length')
    parser.add_argument('-f', dest='filen', help='filename has to be provided', required=True)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
   args = get_args()
   openfile(args.filen)
   sys.exit(0) 
