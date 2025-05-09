#Description:

#Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

#The binary number returned should be a string.
def add_binary(a,b):
    x = a+b
    num=bin(x)
    return (num[2::1])

#def add_binary(a,b):
#    return bin(a+b)[2:]

if __name__ == "__main__":
        add_binary(5,6)
