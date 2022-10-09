

def duplicate(arr,N):

    temp_list=[]
    temp_tuple=[]
    for i in range(0,N) : 
        temp_list.append(0)
    

    for i in range(0,N) : 
        temp=temp_list[arr[i]]
        temp+=1
        temp_list[arr[i]]=temp
        if temp_list[arr[i]]>1 : 
            temp_tuple.append(arr[i])
    return temp_tuple
    


#driver code 
arr=[1,2,2,1]
N=4
print("duplicates -> {}".format(duplicate(arr,N)))
