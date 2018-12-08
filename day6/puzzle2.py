#!/usr/bin/env python3

import sys
import math

def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def print_map(map):
    for y in map:
        for x in y:
            print(x, end="")
        print()

def is_safe(origin, points, safe_distance):
    sum = 0
    for point in points:
        sum += dist(origin, point)
        if sum >= safe_distance:
            break
    if sum < safe_distance:
        return True
    else:
        return False

def closest_point(origin, points):
    if origin in points:
        return origin
    min_distance = math.inf
    min_point = None
    has_tie = False
    for point in points:
        distance = dist(origin, point)
        if distance < min_distance:
            min_distance = distance
            min_point = point
            has_tie = False
        elif distance == min_distance:
            has_tie = True
    if has_tie:
        return None
    else:
        return min_point

def main(input_file):
    SAFE_DISTANCE = 10000

    points = set()
    with open(input_file) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            points.add(tuple(int(x) for x in line.split(", ")))

    min_x = min([x[0] for x in points])
    min_y = min([x[1] for x in points])

    # Define our bounding box. anything ouside of these must be above
    # safe distance
    adjust_min_x = SAFE_DISTANCE - min_x
    adjust_min_y = SAFE_DISTANCE - min_y

    # Create a set of points that are adjusted to limit the number of points
    # to check
    adjusted_points = { (x[0]+adjust_min_x, x[1]+adjust_min_y) for x in points}

    max_x = max([x[0] for x in adjusted_points])
    max_y = max([x[1] for x in adjusted_points])

    print("Max X: {0}".format(max_x))
    # Make our map of points with all points marked as outside the safe zone
    map = [[]] * (max_y+1)
    for i in range(max_y+1):
        map[i] = [False] * (max_x+1)

    # For all points in the box, find the closest point determine if safe
    for y in range(max_y+1):
        for x in range(max_x+1):
            map[y][x] = is_safe((x,y), adjusted_points, SAFE_DISTANCE)

    #print_map(map)
    area = 0
    for y in range(max_y+1):
        for x in range(max_x+1):
            if map[y][x]:
                area += 1

    print("Max Area: {0}".format(area))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input file argument")
    else:
        main(sys.argv[1])
