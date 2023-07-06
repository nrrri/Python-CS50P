## function
# define main
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

# define get_int
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
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