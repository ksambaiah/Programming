th arguments 
Python comes with thousands of modules. Question is what is meant by python module? How to install them?
A Python module is just a file containing Python code, like functions, classes, or variables, which you can use in your own programs by importing it. It helps you organize your code and reuse it easily across different projects.

 You can install python module as
 ```
 pip install modulename
 ```
 sys, random modules are used already with out explanation. We will discuss argparse module.
 

    selectionsort.py 
usage: selectionsort.py [-h] -n LEN [-t TEST]
selectionsort.py: error: the following arguments are required: -n

 Try to run selectionsort.py, it said I should call with -h for help. -n is required argument.
 

    def get_args():
    parser = argparse.ArgumentParser(prog='selectionsort.py', description='selection sort program sorts array of given length')
    parser.add_argument('-n', dest='len', type=int, help='integer has to be provided', required=True)
    parser.add_argument('-t', dest='test',  help='testing if array sorted')
    args = parser.parse_args()
    return args
We defined function get_args function.  Argparse module prog defined by name of the program.
-n arg is used as len, it should be input as integer and required element. If we don't pass value to -n program will not run.
-t is an optional argument, not compulsory.

    python3 selectionsort.py -h
usage: selectionsort.py [-h] -n LEN [-t TEST]

selection sort program sorts array of given length

options:
  -h, --help  show this help message and exit
  -n LEN      integer has to be provided
  -t TEST     testing if array sorted

    python3 selectionsort.py -n 10 -t unittest
Array before sorting of length  10
[1920439370, 3920690398, -9238302398, -5820954739, -7686522432, 9282327505, -1210693909, 6601771457, 1182440262, 3656881098]
Array after sorting
[-9238302398, -7686522432, -5820954739, -1210693909, 1182440262, 1920439370, 3656881098, 3920690398, 6601771457, 9282327505]
Array is sorted order

## Unit test
Your code should go hand in hand with unit test. Very crude test case is mentioned, we will imrpove further.a
