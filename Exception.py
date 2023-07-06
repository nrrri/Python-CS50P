## function
# define main
def main():
    x = get_int()
    print(f"x is {x}")

# define get_int
def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x

# call main
main()

"""
test input
true : 1 (number)
false : cat (string)
"""