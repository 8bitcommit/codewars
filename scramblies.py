#Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

#Notes:

#    Only lower case letters will be used (a-z). No punctuation or digits will be included.
#    Performance needs to be considered.

def scramble(s1, s2):
        for i in s2.lower():
                if (i not in s1.lower()):
                        return False
                x=s1.find(i)
                s1.replace(s1[x],'')
        return True


if __name__ == "__main__":
        scramble('rkqodlw', 'world')
        scramble('cedewaraaossoqqyt', 'codewars')
        scramble('katas', 'steak')

