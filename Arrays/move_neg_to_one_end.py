

def moveNegativeToOneEnd(arr) : 
    negativeList=[]
    positiveList=[]
    for i in range(len(arr)) : 
        if arr[i] < 0 : 
            negativeList.append(arr[i])
        else : 
            positiveList.append(arr[i])
    return negativeList + positiveList

#driver function 
arr=[-3,4,-5,12,-45,32,-90,11,9]
print("list -> {}".format(moveNegativeToOneEnd(arr)))
