#!/usr/bin/env python3

import sys

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

    polymer = react_polymer(polymer)
    print("Final polymer: {0}".format("".join(polymer)))
    print("Unit Count: {0}".format(len(polymer)))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input file argument")
    else:
        main(sys.argv[1])
