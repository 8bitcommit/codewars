

def solution(s):
        x=[]
        if (len(s)%2!=0):
                s  = s+'_'
        count=2
        for i in range(len(s)):
                if (i%2==0):
                        x.append(s[i:count])
                        count+=2
        print(x)


if __name__ == "__main__":
        solution('abcdfghij')
