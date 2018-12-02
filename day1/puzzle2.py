
#!/usr/bin/env python3

import sys

def main(input_file):
    match_found = False
    frequency = 0
    past_frequencies = [0]

    while not match_found:
        with open(input_file) as f:
            while True:
                line = f.readline()
                if not line:
                    break
                frequency += int(line)

                if frequency in past_frequencies:
                    match_found = True
                    break
                else:
                    past_frequencies.append(frequency)

    print("First duplicate frequency: {0}".format(frequency))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input file argument")
    else:
        main(sys.argv[1])
