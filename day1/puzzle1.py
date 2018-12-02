
#!/usr/bin/env python3

import sys

def main(input_file):
    frequency = 0

    with open(input_file) as f:
        while True:
            line = f.readline()
            if not line:
                break

            frequency += int(line)

    print("Frequency: {0}".format(frequency))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input file argument")
    else:
        main(sys.argv[1])
