import sys as sys

def isdigit(string : str) -> bool:
    for i in string:
        if i.isdigit() is False:
            return False
    return True

if len(sys.argv) == 1:
    sys.exit()
elif len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
else:
    if isdigit(sys.argv[1]):
        number_arg = int(sys.argv[1])
        if number_arg % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    else:
        print("AssertionError: argument is not an integer")
