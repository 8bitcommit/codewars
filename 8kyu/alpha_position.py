#In this kata you are required to, given a string, replace every letter with its position in the alphabet.
#If anything in the text isn't a letter, ignore it and don't return it.


def alphabet_position(text):
        txt = text.lower()
        letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
        string = ""
        for i in txt:
                for x,y in zip(letter,nums):
                        if (i == x):
                                string += str(y) + ' '
        print(string[:-1])
              

if __name__ == "__main__":
        alphabet_position("The sunset sets at twelve o' clock.")
        
