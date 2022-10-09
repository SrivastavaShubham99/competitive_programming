


def dutch_segregation(arr) : 
    mid=0
    low=0
    high=len(arr)-1


    while mid <= high : 
        if arr[mid]==0 : 
            arr[low],arr[mid]=arr[mid],arr[low]
            mid=mid+1
            low=low+1
            
        elif arr[mid]==1 : 
            mid=mid+1
            
        else : 
            arr[mid],arr[high]=arr[high],arr[mid]
            high=high-1
    
    return arr
    

   
            

list=[0, 1, 2, 0, 1, 2]
# print("list is -->>> {}".format(segregate(list)))
print("dutch algorith -->> {}".format(dutch_segregation(list)))