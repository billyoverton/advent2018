#!/usr/bin/env python3

import sys
import re

def main(input_file):
    pattern = re.compile("(\#\d+) \@ (\d+),(\d+): (\d+)x(\d+)")

    fabric = {} # (left, top) -> [claims]
    claims = []
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

            claims.append(claim)

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

        for square, owning_claims in fabric.items():
            if "#653" in owning_claims:
                print("{0}: {1}".format(square, owning_claims))
            if len(owning_claims) > 1:
                for claim in owning_claims:
                    if claim in claims:
                        claims.remove(claim)
            if len(claims) == 1:
                break

        print("Non Overlaping Claims: {0}".format(",".join(claims)))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input file argument")
    else:
        main(sys.argv[1])
