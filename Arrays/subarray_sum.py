

def sumarray_sum(arr) : 
    prefix_sum=0
    mapper=set()
    for i in range(len(arr)) : 
        prefix_sum+=arr[i]
        if prefix_sum == 0 or prefix_sum in mapper : 
            return True
        mapper.add(prefix_sum)
    return False

#driver function 

arr=[4 ,2, -3, 1, 6]
print("if sum zero exists -> {}".format(sumarray_sum(arr)))
