#Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.



def is_valid_IP(strng):
    x=strng.split(".")
    for i in x:
        
        if ((len(x)==4) and (i.isnumeric()==True) and (int(i)<256) and (int(i)>=0)):
            continue
        else:
            return False
    return True



