#A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

#Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

def is_pangram(st):
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for i in alpha:
                if (i not in st.lower()):
                        print("NOT")
                        return False
        print("P")
        return True  

#other_solutions
#import string

#def is_pangram(s):
#    return set(string.ascii_lowercase).issubset(s.lower())

if __name__ == "__main__":
       is_pangram("The quick brown fox jumps over the lazy dog.")
       is_pangram("cat.")
