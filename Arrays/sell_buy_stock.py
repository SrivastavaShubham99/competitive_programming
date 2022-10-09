
#brute force approach
def sell_buy_stock(arr) : 
    max_profit=0
    for i in range(len(arr)): 
        for j in range(i,len(arr)) : 
            if(arr[j] - arr[i] > max_profit and arr[j] - arr[i] > 0) : 
                max_profit=arr[j] - arr[i]
    return max_profit


#efficient solution with O(N) with space complexity as O(1)
def sell_buy_efficiently(arr): 
    leftPointer=0
    max_profit=0
    rightPointer=1
    while rightPointer < len(arr) : 
        current_profit=arr[rightPointer]-arr[leftPointer]
        if arr[rightPointer] > arr[leftPointer] : 
            max_profit=max(max_profit,current_profit)
        else : 
            leftPointer=rightPointer
        rightPointer+=1
    return max_profit

        




#driver function ......

arr=[7,1,5,3,6,4]
res=sell_buy_efficiently(arr)
print("soution ->{}").format(res)
