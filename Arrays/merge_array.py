
def merge_array(arr1,n,arr2,m) : 
    p1=0
    p2=0
    
    while p1<len(arr1) : 
        if arr1[p1] < arr2[p2] : 
            p1+=1
            
        else : 
            arr1[p1],arr2[p2]=arr2[p2],arr1[p1]
            arr2.sort()
            p1+=1
            
        

    return arr1+arr2

#driver function 

arr1=[2,5,9,14,19,22,32]
arr2=[4,6,8,11,21]
n=7
m=5
print("sorted array -> {}".format(merge_array(arr1,n,arr2,m)))



