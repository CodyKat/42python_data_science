import sys


def text_analyzer(string=None):

    if string is None:
        print("What is the text to count?")
        string = sys.stdin.readline()

    lower = 0
    upper = 0
    space = 0
    punctuation = 0
    digit = 0

    for i in string:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
        elif i.isspace():
            space += 1
        elif not i.isalnum():
            punctuation += 1
        elif i.isdigit():
            digit += 1

    print(f"The text contains {lower+upper+space+punctuation+digit} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


text_analyzer.__doc__ = """count characters..
        lower case, upper case, punctuation, space, digit"""


def main():
    print(text_analyzer.__doc__)
    if len(sys.argv) > 1:
        text_analyzer(sys.argv[1])
    else:
        text_analyzer()


if __name__ == "__main__":
    main()
