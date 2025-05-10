'''sum list and remove first element'''

def parts_sums(ls):
    sums = [0] * (len(ls) + 1)
    for i in range(len(ls) - 1, -1, -1):
        sums[i] = ls[i] + sums[i + 1]
    return sums


'''def parts_sums(ls):
    sums=[]
    num=0
    while(1):
           for i in ls:
                num+=i
           sums.append(num)
           num=0
           if ls:
                   ls.pop(0)
           else:
                   return sums
'''
if __name__ == "__main__":
        print(parts_sums(ls=[0,1,3,6,10]))
