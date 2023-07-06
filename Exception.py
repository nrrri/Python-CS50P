## function
# define main
def main():
    x = get_int()
    print(f"x is {x}")

# define get_int
def get_int():
    while True:
        try:
            return int(input("What's x? "))
           # x = int(input("What's x? "))
        except ValueError:
            pass
        """
        # same as above but longer
        print("x is not an integer")
        else:
        break
    return x
        """
        

# call main
main()

"""
test input
true : 1 (number)
false : cat (string)
"""