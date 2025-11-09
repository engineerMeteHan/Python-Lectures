print("mete")
print("MEtehan gencer")

c1 = complex(3,4)
c2 = complex(5)
c3 = complex()

print(c1)
print(c2)
print(c3)
print(type(c1))
print(c1.real)
print(c1.imag)
print("-------------------------------------------------------")
print(complex())


c1 = complex(3,4)
print(c1)

c2 = complex(2.5, 3.7)
print(c2)

c1 = complex("5.5")
print(c1)

c2 = complex("-2")
print(c2)

c3 = complex("3+4j")
print(c3)

c1 = complex(4, 3)
c2 = complex(2, -2)

print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)  

# accessing real and imaginary parts
print(c1.real)
print(c1.imag)

d1 = {1: "mete", 2: "gencer"}
print(d1)

# Create dictionary using dict() constructor    
d2 = dict(a = "geeks", b = "nete", c = "metehan")
print(d2)

d = {"name": "metehan", 1: "gencer", (1, 2): [1, 2, 4]}

# access using key 
print(d["name"])
print(d[1])

# Access using get()
print(d.get("name"))
print(d.get(1))

d = {1: "mete", 2: "gencer", 3: "Embedded System Engineer"}

# Adding a new key-value pair
d["age"]  = 36

# updating an existing value
d[1] = "python dict"
print(d)

d = {1: "mete", 2: "gencer", 3: "Embedded System Engineer", "age": 33}
del d["age"]
print(d)

# using pop() method to remove an item and return the value 
val = d.pop(1)
print(val)

key, val = d.popitem()
print(f"key: {key}, value: {val}")

# clear all items from the dictionary
d.clear()
print(d)

d = {1: "geek", 2: "for", "age": 25}

# iterate over keys 
for key in d: 
    print(key, end= " ") 

# iterate over values
for value in d.values():
    print(value, end= " ")
    print("\n---------------------\n")
    print(value)

# example of nested dictionary 
d = {
    "person1": {
        "name": "mete",
        "age": 36,
    },
    "person2": {
        "name": "gencer",
        "age": 30,
    },
}

print(d)

d = {1: "mete", 2: "gencer",
      3: {
          "a": "Embedded",
          "b": "System",
          "c": "Engineer"
      }
     }

print(d)

from collections import Counter
from itertools import combinations

def count_min_subsets(arr):
    freq = Counter(arr)
    num_distinct = len(set(arr))
    if num_distinct == len(arr):
        return 1
    else: 
        for i in range (1, num_distinct + 1):
            for subset in combinations(freq.keys(), i):
                if len(set(subset)) == i:
                    if sum([freq[k] for k in subset]) >= i:
                        return i + 1 

arr = [1, 2, 3, 4]         
print(count_min_subsets(arr))
print("-------------------------------------------------------------------------------------")
def find_Missing(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)  

    for i in range(n1):
        found = False
        for j in range(n2):
            if arr1[i] == arr2[j]:
                found = True
                break
        if not found:
            return arr1[i]    # return the missing element 
    return -1  # return -1 if no missing element found 

# Driver code 
arr1 = [1,4,5,7]
arr2 = [1 ,5,7]

missing = find_Missing(arr1, arr2) 

if missing == -1: 
    print("no missing element")
else: 
    print(f"missing element is: {missing}")

print("New approach for finding missing element")

"""
    PROGRAM DESCRIPTION:
    python3 program to find missing elemnent 
    from same arrays (except one missing element)
"""

"""
    FUNCTION DEFINITIONS:
    Function to find missing element based 
    on binary search approach. arr1[] is 
    of larger size and N is size of it. 
    arr1[] and arr2[] are assumed to be same order 
"""
def findMisiingUtil(arr1, arr2, N):

    # Special case, for only element
    # which is missing in second array

    if N == 1: 
        return arr1[0]
    
    # Special case, for first element missing
    if arr1[0] != arr2[0]:
        return arr1[0]
    
    # initialize current corner points 
    lo = 0 
    hi = N - 1

    # loop until lo < hi 
    while (lo < hi):
        mid = (lo + hi) / 2 

        # if elemnt at mid indices are equal then go to right subarray 
        if arr1[mid] == arr2[mid]:
            lo = mid
        else: 
            hi = mid


        # if lo, hi becomes contiguous, break
        if lo == hi - 1:
            break

    # missing element will be at hi index of bigger array 
    return arr2[hi]

"""
    Function description:
    This function mainly deos basic error 
    checking and calls findMissingUtil()
"""

def findMissing(arr1, arr2, M, N):
    if N == M - 1:
        print("Missing element is: ", findMisiingUtil(arr1, arr2, M))
    elif M == N - 1:
        print("Missing element is: ", findMisiingUtil(arr2, arr1, N))
 
    else: 
        print("Invalid input")

# Driver code   
arr1 = [1,4,5,7,9]
arr2 = [4,5,7,9]

M = len(arr1)
N = len(arr2)
findMissing(arr1, arr2, M, N)
print("-----------------------------------------------------")

def isHeterogram(s, n):
    hash = [0] * 26 

    # traversing the string 
    for i in range(n):

        # ignore the space 
        if s[i] != ' ':
 
            # if already encountered 
            if hash[ord(s[i]) - ord('a')] == 0:
                hash[ord(s[i]) - ord('a')] = 1

            # else return false
            else: 
                return False
    return True

# Driven Code   
s = "the big dwarf only jumpss"
n = len(s)
print("YES" if isHeterogram(s,n) else "NO")





