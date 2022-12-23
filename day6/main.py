# link - https://adventofcode.com/2022/day/6

def calculate_part1():
    with open('./input.txt', 'r') as data_file:
        input_lines = data_file.readlines()[0]
        marker_loc = 4
        for index in range(4, len(input_lines)):
            set_len = set(input_lines[index-4: index])
            if len(set_len) == 4:
                marker_loc=  index
                break
        print('part1 answer: ', marker_loc)

def calculate_part2():
    with open('./input.txt', 'r') as data_file:
        input_lines = data_file.readlines()[0]
        marker_loc = 14
        for index in range(14, len(input_lines)):
            set_len = set(input_lines[index-14: index])
            if len(set_len) == 14:
                marker_loc=  index
                break
        print('part2 answer: ', marker_loc)


if __name__ == '__main__':
    calculate_part1()
    calculate_part2()