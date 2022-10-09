
def inversion_count(arr) : 
    currentPointer=0
    fastMovingPointer=currentPointer+1
    count=0

    while currentPointer<len(arr) : 
        if(fastMovingPointer>=len(arr)-1 and fastMovingPointer<len(arr)) : 
            currentPointer+=1
            fastMovingPointer=currentPointer+1
          
        if(arr[currentPointer]>arr[fastMovingPointer]) : 
            count+=1
            fastMovingPointer+=1
            print("fast moving pointer 1-> {}".format(fastMovingPointer))
        else :  
            fastMovingPointer+=1
        
    return count


#driver functions : 
arr=[2,4,1,3,5]
print("inversion count -> {}".format(inversion_count(arr)))

    