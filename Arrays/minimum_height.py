

def min_height(arr,n,k) : 

    arr.sort()
    res=arr[n-1]-arr[0]
    min_height=arr[0]
    max_height=arr[n-1]
    
    for i in range(1,n) : 

        if arr[i]-k<0 : 
            continue

        max_height=max(arr[i-1]+k,arr[n-1]-k)
        min_height=min(arr[0]+k,arr[i]-k)
        return min(res,max_height-min_height)

#driver function 
arr=[2 ,6 ,3, 4 ,7, 2, 10, 3 ,2 ,1]
n=10
k=2
print("min height -> {}".format(min_height(arr,n,k)))
