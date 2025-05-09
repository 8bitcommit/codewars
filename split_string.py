

def solution(s):
        x=[]
        if (len(s)%2!=0):
                s  = s+'_'
        for i in range(len(s)):
                if (i%2==0):
                        x.append(s[i:i+2])
        return(x)


if __name__ == "__main__":
        solution('abcdfghij')
