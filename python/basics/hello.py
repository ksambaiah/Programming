#!/usr/bin/env python

# This is my first program

print("Hello, world")
print("5 + 3")
variable = 5 + 3
print(variable)

i = 7
j = 10
print("i + j are %d, %d, %d" %(i,j,i+j))
print("i * j are %d, %d, %d" %(i,j,i*j))
i = 7.1
j = 10.2
print("i + j are %f, %f, %f" %(i,j,i+j))
print("i * j are %f, %f, %f" %(i,j,i*j))

s = "Lakshmi Sojanya"
print("Length of string s is ", len(s))
print(s)
print("2'nd element of s", s[2])

j = "kilaru"

Name = s + " " + j
print(Name)

arr = [1, 2, 10, "lakshmi", 4, -2.3]
print(len(arr))

for x in arr:
    print(x)

subarr = arr[:3]
print(subarr)
print(arr)
