

def reverseWord(s):
    list=[]
    character=''
    for i in range(len(s)):
        list.append(s[i])
    for i in range(len(s)-1,-1,-1) :
        character+=s[i]
    return character

