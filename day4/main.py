# link - https://adventofcode.com/2022/day/4


def calculate_part1():
    with open('./input.txt', 'r') as data_file:
        input = data_file.readlines()
        overlap_count = 0
        for line in input:
            elf1, elf2 = line.split(',')
            elf1_index1, elf1_index2 = elf1.split('-')
            elf2_index1, elf2_index2 = elf2.split('-')
            if int(elf1_index1)>=int(elf2_index1) and int(elf1_index2)<=int(elf2_index2):
                overlap_count += 1
            elif int(elf1_index1)<=int(elf2_index1) and int(elf1_index2)>=int(elf2_index2):
                overlap_count+= 1
            print('fafa', elf1_index1, elf1_index2, elf2_index1, elf2_index2, overlap_count)
        
        print('part1 overlaps: ', overlap_count)

def calculate_part2():
    with open('./input.txt', 'r') as data_file:
        input = data_file.readlines()
        overlap_count = 0
        for line in input:
            elf1, elf2 = line.split(',')
            elf1_index1, elf1_index2 = [int(value) for value in elf1.split('-')]
            elf2_index1, elf2_index2 = [int(value) for value in elf2.split('-')]
            if elf1_index1 in range(elf2_index1, elf2_index2+1) or elf1_index2 in range(elf2_index1, elf2_index2+1):
                overlap_count+= 1
            elif elf2_index1 in range(elf1_index1, elf1_index2+1) or elf2_index2 in range(elf1_index1, elf1_index2+1):
                overlap_count+= 1
        print('part2 answer: ', overlap_count)


if __name__ == '__main__':
    # calculate_part1()
    calculate_part2()