import random    #Question 5.1 - Generating random input array of size n

def genRandomArray(n):  
    A = []
    for i in range(n):
        A.append(random.randint(0,999))
    return A

size = int(input("Enter the size of the array A "))
A = genRandomArray(size)
print(f"The array A = {A}")

#  --------------------------This belongs to a seperate file ----------------------------------------

import Q5_1
from Q5_1 import A
import time
def implementSort(A,B):   #Question 5.2 - implementation of sorting algorithm
    start = time.time()
    largest = float('-inf')
    idx = -1
    lastIndex = len(B)-1
    while lastIndex>=0:
        for i in range(len(A)):
            if A[i]>largest:
                largest = A[i]
                idx = i
        B[lastIndex] = largest
        largest = float('-inf')
        A[idx] = largest
        lastIndex-=1
    end = time.time()
    print(end-start)  #Question 5.3 - To determine the total run time of the algorithm
    return B

B = [None] * len(A)
result = implementSort(A,B)
print(f"The sorted array B = {result}")   
        
