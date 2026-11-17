"""Shift English letters by a chosen number of places."""

import argparse
import string


def encrypt(message, shift):
    alphabet = string.ascii_uppercase
    result = []
    for letter in message.upper():
        if letter in alphabet:
            position = (alphabet.index(letter) + shift) % len(alphabet)
            result.append(alphabet[position])
        else:
            result.append(letter)
    return "".join(result)


def decrypt(message, shift):
    return encrypt(message, -shift)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("message")
    parser.add_argument("shift", type=int)
    parser.add_argument("--decrypt", action="store_true")
    args = parser.parse_args()
    operation = decrypt if args.decrypt else encrypt
    print(operation(args.message, args.shift))


if __name__ == "__main__":
    main()
