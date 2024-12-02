import time


def parse_input(filename):
    directions = []
    with open(filename) as inp:
        for line in inp:
            directions.append([(x[0], int(x[1:])) for x in line.strip().split(",")])
        directions_wire_1 = directions[0]
        directions_wire_2 = directions[1]
    return directions_wire_1, directions_wire_2


def map_coordinates(directions, start=(0,0)):
    direction_dict = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
    coordinates = []
    current_coordinate = start
    for direction_set in directions:
        direction, steps = direction_set
        direction_tuple = direction_dict[direction]
        for i in range(steps):
            current_coordinate = (current_coordinate[0] + direction_tuple[0], current_coordinate[1] + direction_tuple[1])
            coordinates.append(current_coordinate)
    return coordinates


def find_intersections(coordinates_wire_1, coordinates_wire_2):
    return list(set(coordinates_wire_1).intersection(coordinates_wire_2))


def find_lowest_distance(coordinates):
    manhattan_distances = []
    for coordinate in coordinates:
        a, b = coordinate
        manhattan_distances.append(abs(a) + abs(b))
    manhattan_distances.sort()
    return manhattan_distances[0]


def find_least_steps(intersections, coordinates_wire_1, coordinates_wire_2):
    lowest = -1
    for intersection in intersections:
        steps_1 = coordinates_wire_1.index(intersection) + 1
        steps_2 = coordinates_wire_2.index(intersection) + 1
        sum_distances = steps_1 + steps_2
        if sum_distances < lowest or lowest == -1:
            lowest = sum_distances
    return lowest


def main(filename):
    start_time = time.time_ns()

    # parse input
    directions_wire_1, directions_wire_2 = parse_input(filename)
    coordinates_wire_1 = map_coordinates(directions_wire_1)
    coordinates_wire_2 = map_coordinates(directions_wire_2)
    intersections = find_intersections(coordinates_wire_1, coordinates_wire_2)

    # Part 1
    lowest_manhattan = find_lowest_distance(intersections)
    print(f"The lowest manhattan distance is: {lowest_manhattan}")

    # part 2
    lowest_steps = find_least_steps(intersections, coordinates_wire_1, coordinates_wire_2)
    print(f"The lowest amount of steps is: {lowest_steps}")
    print("--- %s ms ---" % ((time.time_ns() - start_time) / 1000000))


main("input/day03_short.txt")
main("input/day03.txt")
