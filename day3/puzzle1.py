#!/usr/bin/env python3

import sys
import re

def main(input_file):
    pattern = re.compile("(\#\d+) \@ (\d+),(\d+): (\d+)x(\d+)")

    fabric = {} # (left, top) -> [claims]

    with open(input_file) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            m = pattern.match(line)

            # Get our claim properties
            claim = m.group(1)
            left = int(m.group(2))
            top = int(m.group(3))
            width = int(m.group(4))
            height = int(m.group(5))

            current_top = top
            for y in range(height):
                current_left = left
                for x in range(width):
                    if (current_left, current_top) in fabric:
                        fabric[(current_left, current_top)].append(claim)
                    else:
                        fabric[(current_left, current_top)] = [claim]
                    current_left += 1
                current_top += 1

        overlap_count = 0
        for square, claims in fabric.items():
            if len(claims) > 1:
                overlap_count += 1

        print("Overlap Count: {0}".format(overlap_count))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input file argument")
    else:
        main(sys.argv[1])
