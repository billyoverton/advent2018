
#!/usr/bin/env python3

import sys

def main(input_file):
    count_2 = 0
    count_3 = 0
    with open(input_file) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            chars = {}
            match_2 = False
            match_3 = False
            for char in line:
                if char in chars:
                    chars[char] += 1
                else:
                    chars[char] = 1


            for char, value in chars.items():
                if value == 2 and not match_2:
                    count_2 += 1
                    match_2 = True

                if value == 3 and not match_3:
                    count_3 += 1
                    match_3 = True
            print(chars)
    print("checksum is {0}".format(count_2 * count_3))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input file argument")
    else:
        main(sys.argv[1])
