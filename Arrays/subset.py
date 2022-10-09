
#time complexity O(N^2)
#for every element we are searching in the list which takes O(N) 

def subset(arr1,arr2) : 
    for i in range(len(arr2)) : 
        if search_element(arr2[i],arr1) : 
            continue
        else : 
            return False
    return True


def search_element(value,arr) : 
    for i in range(len(arr)-1) : 
        if arr[i]==value : 
            return True
        else : 
            continue
    return False




#driver function 
arr1=[3,4,66,32,11,67,54,21]
arr2=[4,5,54]
print("res -> {}".format(subset(arr1,arr2)))