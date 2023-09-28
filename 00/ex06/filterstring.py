import sys


def isdigit(string: str) -> bool:
    for i in string:
        if i.isdigit() is False:
            return False
    return True


def main():
    if len(sys.argv) < 3 or len(sys.argv) > 3:
        print("AssertionError: the arguments are bad")
    elif isdigit(sys.argv[2]) is False:
        print("AssertionError: the arguments are bad")
    else:
        S = sys.argv[1].split(' ')
        N = int(sys.argv[2])
        words = [word for word in S if (lambda word: len(word) > N)(word)]
        print(words)


if __name__ == "__main__":
    main()
