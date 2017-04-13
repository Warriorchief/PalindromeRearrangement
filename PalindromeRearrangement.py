def palindromeRearranging(inputString):
    w=''.join(sorted(inputString))     
    if w==inputString and len(w)%2==1: #edge case:string consists of only one unique character
        return True  
    if len(w)%2==0:
        for char in w:
            if w.count(char)%2!=0:
                return False
        return True
    else: #if string is odd num of chars
        flag=False #marks whether the single-occurrence char has been seen yet
        for char in w:
            if w.count(char)%2!=0:
                if flag:
                    return False
                else:
                    flag=True
        return True

"""   
a='madam'
b='racecar'
c='amanaplanacanalpanamarrrrff'
d='zzzz'
e='ppppp'

print(palindromeRearranging("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc"))
"""
