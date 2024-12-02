import time


def find_version(filename):
    # meuk voor print statements

    if filename.find("short") > 0:
        version = "test input"
    else:
        version = "actual input"
    return version


def parse_input(filename):
    with open(filename) as inp:
        lines = [int(x) for x in inp.read().split(",")]
    return lines


def replace_values(integer_string, address, new_value):
    integer_string[address] = new_value
    return integer_string


def execute_instructions(memory, instruction_size=4):
    for i in range(0, len(memory) + 1, instruction_size):
        opcode = memory[i]
        new_value = 0
        
        # return when opcode is exit
        if opcode == 99:
            return memory[0]

        # assign values
        value_1 = memory[memory[i + 1]]
        value_2 = memory[memory[i + 2]]
        return_address = memory[i + 3]

        if opcode == 1:
            new_value = value_1 + value_2
        elif opcode == 2:
            new_value = value_1 * value_2
        if opcode > 2:
            print("program not working")
            return memory[0]

        memory[return_address] = new_value
    return memory[0]


def find_noun_verb(target_value, memory):
    working_memory = memory.copy()
    for i in range(0, 100, 1):
        noun = i
        for j in range(0, 100, 1):
            verb = j
            # replace with values
            working_memory = replace_values(working_memory, 1, noun)
            working_memory = replace_values(working_memory, 2, verb)
            output = execute_instructions(working_memory)
            if output == target_value:
                return noun, verb
            working_memory = memory.copy()

    # execute instructions


def main(filename):
    start_time = time.time_ns()
    version = find_version(filename)

    # parse input
    memory = parse_input(filename)
    # original_memory = memory.copy()
    noun, verb = find_noun_verb(19690720, memory)
    print(100 * noun + verb)
    print("--- %s ms ---" % ((time.time_ns() - start_time) / 1000000))


main("input/day02.txt")
