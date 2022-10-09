

def kthSmallest(arr,k) : 
    arr.sort()
    return arr[k-1]

#driver function 
arr=[4,6,78,32,89,120]
k=4
print("kth smallest element -> {}".format(kthSmallest(arr,k)))
