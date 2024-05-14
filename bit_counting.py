#Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

#Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

def count_bits(n):
    binary = bin(n)
    x = 0
    for i in binary:
        if i == "1":
            x += 1
    return x


#def solution(s):
#    return ''.join(' ' + c if c.isupper() else c for c in s)
