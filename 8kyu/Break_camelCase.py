#Complete the solution so that the function will break up camel casing, using a space between words.

def solution(s):
    new =''
    for i in s:
        if i.isupper()==True:
            new += ' ' + i
        else:
            new+=i
    return new


#def solution(s):
    #return ''.join(' ' + c if c.isupper() else c for c in s)
