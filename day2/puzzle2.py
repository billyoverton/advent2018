
#!/usr/bin/env python3

import sys
def get_count_diff(string1, string2):
    diff = 0
    diff_index = -1
    for index, char in enumerate(string1):
        if string2[index] != char:
            diff += 1
            diff_index = index
        if diff >= 2:
            return (diff, 0)
    return (diff, diff_index)

def main(input_file):
    boxes = []
    with open(input_file) as f:
        boxes = [x.strip() for x in f.readlines()]

    found = False
    while not found:
        box = boxes.pop()
        for comp_box in boxes:
            diff, index = get_count_diff(box, comp_box)
            if diff == 1:
                # we found two boxes with one difference
                print("Matching boxes found:")
                print(box)
                print(comp_box)
                print("{0}{1}".format(box[:index], box[index+1:]))
                found = True
                break

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input file argument")
    else:
        main(sys.argv[1])
