import time
from math import floor

def find_version(filename):
    # meuk voor print statements

    if filename.find("short") > 0:
        version = "test input"
    else:
        version = "actual input"
    return version


def parse_input(filename):
    with open(filename) as inp:
        lines = [int(x) for x in inp.readlines()]
    return lines


def fuel_requirements(mass):
    fuel = floor(mass / 3) - 2
    return fuel


def main(filename):
    start_time = time.time_ns()
    version = find_version(filename)

    # parse input
    module_masses = parse_input(filename)

    # pt 1
    sum_fuel_req = 0
    for mass in module_masses:
        sum_fuel_req += fuel_requirements(mass)

    print(f"fuel requirement {version}: {sum_fuel_req}")
    print("--- %s ms ---" % ((time.time_ns() - start_time) / 1000000))



main("input/day01_short.txt")
# main("input/day01.txt")
