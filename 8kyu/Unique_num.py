#where is an array with some numbers. All numbers are equal except for one. Try to find it!

#find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
#find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

def find_uniq(arr):
        new=[]
        for i in arr:
                if i not in new:
                        new.append(i)
        if (arr.count(new[0])==1):
                return new[0]
        else:
                return new[1]

if __name__ == "__main__":
        print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))
        print(find_uniq([ 0, 0, 0.55, 0, 0 ]))
