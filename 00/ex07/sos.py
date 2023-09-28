import sys

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ' ':  '/'}


def sos():
    assert len(sys.argv) == 2, 'the arguments are bad'
    string = sys.argv[1].upper()
    output = []

    for i in string:
        assert i in MORSE_CODE_DICT, 'the arguments are bad'
        output.append(MORSE_CODE_DICT[i])

    for i in range(len(output)):
        print(output[i], end='')
        if (i in range(len(output) - 1)):
            print(' ', end='')


sos.__doc__ = """sos print MORSE CODE"""


if __name__ == "__main__":
    sos()
