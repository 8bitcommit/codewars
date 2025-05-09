#A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

#For example, take 153 (3 digits), which is narcissistic:
def narcissistic( value ):
        sum=0
        string=str(value)
        exp= len(string)
        
        for i in range(exp):
                num=int(string[i])
                sum+=num**exp
        print(sum == int(value))
        return sum == int(value)
#solution
#def narcissistic(value):
#    return value == sum(int(x) ** len(str(value)) for x in str(value))

if __name__ == "__main__":
        narcissistic(153)
        narcissistic(1652)
