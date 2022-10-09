

def cyclic_rotate(arr) : 
    last=arr[len(arr)-1]
    for i in range(len(arr)-1,0,-1) : 
        arr[i]=arr[i-1]
    arr[0]=last
    return arr

#driver function 
arr=[1, 2, 3, 4, 5]
print("ratation by one -> {}".format(cyclic_rotate(arr)))