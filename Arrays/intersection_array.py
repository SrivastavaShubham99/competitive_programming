

def union(arr,arr2) : 
    set1=set(arr)
    set2=set(arr2)
    set1.intersection(set2)
    return len(set1)

def union2(arr,arr2) : 
    setter=set()
    for i in range(len(arr)) :
        setter.add(arr[i])
    
    for i in range(len(arr2)) : 
        setter.add(arr2[i])

    return len(setter)

arr=[85, 25, 1, 32, 54 ,6]
arr2=[85,2]
print("union of arr and arr2 -> {}".format(union2(arr,arr2)))
