

def factorial_number(n) : 
    if n==0 : 
        return 0
    elif n==1 : 
        return 1
    else : 
        return factorial_number(n-1)*n

def factorial2(n) : 
    factorial=1
    for i in range(1,n+1) : 
        factorial*=i
    
    return factorial



#driver function 
n=4
print("factorial is -> {}".format(factorial2(n)))