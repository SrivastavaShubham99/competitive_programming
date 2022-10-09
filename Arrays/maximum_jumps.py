

def maximum_jumps(arr) : 
    jumpCount=0
    jumpSum=0
    currentIndex=0

    while jumpSum < len(arr) : 
        currentIndex=arr[jumpSum] 
        jumpSum+=currentIndex
        jumpCount+=1
    return jumpCount-1

#driver functions 
arr=[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print("maximun jumps are -> {}".format(maximum_jumps(arr)))