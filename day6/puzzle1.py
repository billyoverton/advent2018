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
    points = set()
    with open(input_file) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            points.add(tuple(int(x) for x in line.split(", ")))

    min_x = min([x[0] for x in points])
    min_y = min([x[1] for x in points])

    # Create a set of points that are adjusted to limit the number of points
    # to check
    adjusted_points = { (x[0]-min_x, x[1]-min_y) for x in points}

    max_x = max([x[0] for x in adjusted_points])
    max_y = max([x[1] for x in adjusted_points])

    # Make our map of points with all points unowned
    map = [[]] * (max_y+1)
    for i in range(max_y+1):
        map[i] = [None] * (max_x+1)

    # For all points in the box, find the closest point
    for y in range(max_y+1):
        for x in range(max_x+1):
            map[y][x] = closest_point((x,y), adjusted_points)

    # Get a set of the infinite points
    infinite_points = set()

    # all points on the edge are infinite
    # left and right edge
    for i in range(max_y + 1):
        infinite_points.add( map[i][0] )
        infinite_points.add( map[i][max_x])

    # top and bottom
    for i in range(max_x + 1):
        infinite_points.add( map[0][i] )
        infinite_points.add( map[max_y][i])

    non_infinite_points = adjusted_points - infinite_points

    max_area = 0
    max_adjusted_point = None
    for point in non_infinite_points:
        area = 0
        for y in range(max_y+1):
            for x in range(max_x+1):
                if map[y][x] == point:
                    area += 1
        if area > max_area:
            max_area = area
            max_adjusted_point = point

    # Unadjust point - because I want to
    max_point = (max_adjusted_point[0]+min_x, max_adjusted_point[1]+min_y)

    print("Max Area: {0}".format(max_area))
    print("Max Point: ({0}, {1})".format(max_point[0], max_point[1]))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input file argument")
    else:
        main(sys.argv[1])
