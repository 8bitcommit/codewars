'''
returns all numbers up to x, described as even or odd
'''
def is_odd(x):
        for i in range(x):
                if (i%2==0):
                        if i>0:
                                print(f"{i} is an even number.")
                else:
                        print(f"{i} is an odd number.")

if __name__ == "__main__":
        is_odd(14)
