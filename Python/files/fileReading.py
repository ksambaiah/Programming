#!/usr/bin/env python3
import sys
import argparse

""" This program opens file for reading, and do some thing and exits """

def openfile(filen):
    try:
        with open(filen, 'r') as f:
            data = f.read()
            print(data)
    except FileNotFoundError:
        print("File not found!")
        sys.exit(100)
    except IOError as e:
        print("An error occurred:", e)
<<<<<<< HEAD
    finally:
       if f:
           f.close()
=======
        sys.exit(101)
>>>>>>> 267e4106e8cb40ade434925254a9658e4e1eb3b1


def get_args():
    parser = argparse.ArgumentParser(prog=sys.argv[0], description='File need to be passed')
    parser.add_argument('-f', dest='filen', help='filename has to be provided', required=True)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
   args = get_args()
   openfile(args.filen)
   sys.exit(0) 
