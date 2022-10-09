

def kadane_algorithm(arr) : 
    prevSum=-9999999999
    sum=0
    for i in range(len(arr)) : 
        sum+=arr[i]
        if(prevSum < sum) : 
            prevSum=sum
        elif sum < 0 : 
            sum=0
    return prevSum


def kadane_approach2(arr) : 
    best_sum=-9999999999
    current_sum=0
    for i in range(len(arr)-1) : 
        current_sum=max(arr[i],arr[i]+current_sum)
        best_sum=max(current_sum,best_sum)
    return best_sum

def sumhere() : 
    pass


#driver function 
arr=[-2 ,1 ,-3, 4, -1, 2, 1 ,-5, 4]
print("maximum contiguos subarray -> {}".format(kadane_approach2(arr)))
