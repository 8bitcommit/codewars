#ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything 
#but exactly 4 digits or exactly 6 digits.

#If the function is passed a valid PIN string, return true, else return false.

def validate_pin(pin):
        x=0 
        if (len(pin)==0):
            return False
        for c in range(len(pin)):
                if (((len(pin)==4)or(len(pin)==6))) and (pin[c].isdigit()):
                        x+=1
                        if len(pin)== x:
                                return True
    
                else:
                        return False
#def validate_pin(pin):
#    return len(pin) in (4, 6) and pin.isdigit()

if __name__ == "__main__":
        validate_pin("1ABCD3")
