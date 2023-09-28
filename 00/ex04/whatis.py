import sys as sys


if len(sys.argv) == 1:
    sys.exit()
assert len(sys.argv) == 2, "more than one argument is provided"

num = 0
try:
    num = int(sys.argv[1])
except ValueError:
    raise AssertionError('argument is not an integer')
if num % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
