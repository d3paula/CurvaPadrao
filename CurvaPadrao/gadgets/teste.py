import math
import os 
import sys
arr=[5,3,1,2,4]

arr.sort()
ratio=len(arr)%2
pos=0
if ratio==0:
    pos=int(len(arr)/2)
    median=(arr[pos]+arr[pos+1])/2
else:
    print(len(arr))
    pos=int((len(arr)+1)/2)
    print(pos)
    median=arr[pos-1]

print (median)