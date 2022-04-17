import sys

def insertSorted(arr, n, key):

    # Cannot insert more elements if n is
    # already more than or equal to capacity
    

    i = 0
    while i < len(arr):
        if(arr[i] >  key):
            arr.insert(i, key)
            return len(arr)
        i+=1
    
    arr.append(key)    
    return len(arr)


array = [2,8,15,20,30,50,70]


n = len(array)
key = 100

for i in range(n):
    print("Before insertion", array[i])


c = insertSorted(array, n, key)

for i in range(c):
    print("After insertion", array[i])

    

