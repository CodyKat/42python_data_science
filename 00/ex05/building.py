import sys


def text_analyzer(string=None):
    """count characters..
        lower case, upper case, punctuation, space, digit"""
    if string is None:
        print("What is the text to count?")
        string = sys.stdin.readline()

    lower = 0
    upper = 0
    space = 0
    punc = 0
    digit = 0

    for i in string:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
        elif i.isspace():
            space += 1
        elif not i.isalnum():
            punc += 1
        elif i.isdigit():
            digit += 1

    print(f"The text contains {lower+upper+space+punc+digit} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punc} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def main():
    if len(sys.argv) == 1:
        text_analyzer()
    else:
        assert len(sys.argv) == 2, 'Argument count must be 1 or 0'
        text_analyzer(sys.argv[1])


if __name__ == "__main__":
    main()
