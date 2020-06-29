#!/usr/bin/env python

# Given Set A and Set B A-B is all elements in A but not in B
# Example A = {1,2,3,4,10} B = {"a", 2, 3, 10}
# A - B = { 1,4} with python sets it is easy to have set based operations


if __name__ == "__main__":
    A = {1,2,3,100,6,100,50}
    B = {6,50, "a", "b", 3}
    print("Printing A-B and B-A")
    print(A.difference(B)) # 100 appears only once why
    print(B.difference(A))

    # Union of two two sets
    print("A union B, which is also same as B union A")
    print(A.union(B))
    print(B.union(A))

    #Intersection of A and B
    print("A intersection B and B intersection A, both are same")
    print(A.intersection(B))
    print(B.intersection(A))
