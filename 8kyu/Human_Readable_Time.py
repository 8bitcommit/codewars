#Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

#    HH = hours, padded to 2 digits, range: 00 - 99
#    MM = minutes, padded to 2 digits, range: 00 - 59
#    SS = seconds, padded to 2 digits, range: 00 - 59

#The maximum time never exceeds 359999 (99:59:59)

#You can find some examples in the test fixtures.



def make_readable(seconds):
    h = seconds/3600
    hh = round(seconds//3600)
    m = (h-hh)*3600/60
    mm = round((h-hh)*3600//60)
    s = round((m-mm)*60)
    hrf ='{:02}'.format(hh) +":"+'{:02}'.format(mm)+":"+'{:02}'.format(s)
    return hrf 

if __name__ == "__main__":
        make_readable(359999)
