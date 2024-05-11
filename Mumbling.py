#accum("abcd") -> "A-Bb-Ccc-Dddd"
#accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
#accum("cwAt") -> "C-Ww-Aaa-Tttt"


def accum(st):
    mumble = ''
    for c in range(len(st)):
        if (c==0):
                mumble += st[c].upper()
        else:
                mumble += '-'
                mumble += st[c].upper()
                for i in range(c):
                        mumble += st[c].lower()
    return mumble

#other solutions

#def accum(s):
#    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

#def accum(s):
#    value = ""
#    for i,c in enumerate(s):
#        value += c.upper() + c.lower()*i + "-"
#    return value[:-1]
if __name__ == "__main__":
        accum("RqaEzty")
