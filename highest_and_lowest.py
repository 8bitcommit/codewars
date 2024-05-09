#In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.


def high_and_low(numbers):
        temp_min = 10000000
        temp_max = -10000000
        nums = numbers.split(' ')
        for i in nums:
                if (int(i)>temp_max):
                        temp_max =int(i)
                if (int(i)<temp_min):
                        temp_min = int(i)
        string = str(temp_max) + ' ' + str(temp_min)

        return string

def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))
