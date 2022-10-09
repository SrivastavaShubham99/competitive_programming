

def merge_intervals(Intervals) :
    if len(Intervals)==0 or len(Intervals)==1 : 
        return Intervals

    Intervals.sort(key=lambda x : x[0])
    result=[Intervals[0]]

    for interval in Intervals[1:] : 
        if result[-1][1] >= interval[0] : 
            result[-1][1]=max(result[-1][1],interval[1])
        else : 
            result.append(interval)
    return result

#driver function

arr=[[6,8],[1,9],[2,4],[4,7]]
print("merge intervals -> {}".format(merge_intervals(arr)))
