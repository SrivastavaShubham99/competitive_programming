

def minmax(list) : 
    prevSum=0
    prevSub=12000000000000000
    for i in range(len(list)) : 
        if list[i] > prevSum : 
            prevSum=list[i]

    for i in range(len(list)) : 
        if list[i] < prevSub : 
            prevSub=list[i]
        
    return prevSum,prevSub



list=[3,5,9,1,2,4]
print("max element in the arrray is : {}".format(minmax(list)))
