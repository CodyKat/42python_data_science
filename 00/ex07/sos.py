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


def main():
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        sys.exit()
    string = sys.argv[1].upper()
    output = []

    for i in string:
        try:
            output.append(MORSE_CODE_DICT[i])
        except BaseException:
            print("AssertionError: the arguments are bad")
            sys.exit()

    for i in range(len(output)):
        print(output[i], end='')
        if (i in range(len(output) - 1)):
            print(' ', end='')


if __name__ == "__main__":
    main()
