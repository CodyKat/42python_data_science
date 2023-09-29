import sys


def filterstring():
    assert len(sys.argv) == 3, 'the arguments are bad'
    N = 0
    try:
        N = int(sys.argv[2])
    except ValueError:
        raise AssertionError('the arguments are bad')
    S = sys.argv[1].split(' ')
    words = [word for word in S if (lambda word: len(word) > N)(word)]
    print(words)


filterstring.__doc__ = """input S and N.

program should output a list of words from S
that have a length greater than N."""


if __name__ == "__main__":
    filterstring()
