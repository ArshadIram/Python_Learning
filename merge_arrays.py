
def merge(array1, array2, array3):
    n = len(array1) - 1
    m = len(array2) - 1
    minLen = min(len(array1), len(array2))
    i = 0
    j = 0
    k = 0
    while(i < minLen or j < minLen):
        print(i,j,k)
        if (array1[i]<array2[j]):
            array3[k]=array1[i]
            k+=1
            i+=1
            
        else: 
            array3[k] = array2[j]
            j+=1
            k+=1
    maxArray = array1 if len(array1) > len(array2) else array2

    for a in range(minLen, len(maxArray)):
        array3[k] = maxArray[a]
        k+=1

    return array3
        

array1=[2,3,4,5,6,10, 11] # total 6 
array2 = [1,4,5,6,7] # total 5
n = len(array1)
m= len(array2)
total = n+m
array3 = [None] * total
print(array3)

print(merge(array1,array2,array3))

    
    
