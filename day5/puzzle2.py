#!/usr/bin/env python3

import sys
import string

def react_polymer(polymer):
    lst = list(polymer)
    reaction_occured = True
    while reaction_occured:
        reaction_occured = False
        char = 0
        while char < len(lst) - 1:
            if abs(ord(lst[char]) - ord(lst[char+1])) == 32:
                reaction_occured = True
                lst.pop(char+1)
                lst.pop(char)
            char+=1
    return "".join(lst)

def main(input_file):
    polymer = None
    with open(input_file) as f:
        polymer = f.readline().strip()
        if not polymer:
            print("ERROR: Can't read input string")
            sys.exit(1)

    lowest_value = 1000000
    lowest_char = None
    for char in string.ascii_uppercase:
        new_polymer = polymer.replace(char, "")
        new_polymer = new_polymer.replace(char.lower(), "")
        reacted = react_polymer(new_polymer)
        if len(reacted) < lowest_value:
            lowest_char = "{0}/{1}".format(char, char.lower())
            lowest_value = len(reacted)

    print("Char: {0}".format(lowest_char))
    print("Length: {0}".format(lowest_value))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input file argument")
    else:
        main(sys.argv[1])
