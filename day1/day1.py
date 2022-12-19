# link - https://adventofcode.com/2022/day/1


def calculate_part1():
    with open('../data/day1.txt', mode='r') as data_file:
        lines = data_file.readlines()
        max_calories = 0 # Since calories are not in negative, it won't sum to negative max value
        current_calories = 0
        for line in lines:
            if line == '\n':
                max_calories = max(max_calories, current_calories)
                current_calories = 0
            else:
                current_calories += int(line)

        print('max_calories: ', max_calories)


def calculate_part2():
    with open('../data/day1.txt', mode='r') as data_file:
        lines = data_file.readlines()
        max1, max2, max3 = 0, 0, 0
        current_calories = 0
        for line in lines:
            if line == '\n':
                if current_calories > max1:
                    max3 = max2
                    max2 = max1
                    max1 = current_calories
                elif current_calories > max2 and max1 > current_calories:
                    max3 = max2
                    max2 = current_calories
                elif current_calories > max3 and max2 > current_calories:
                    max3 = current_calories
                current_calories = 0
            else:
                current_calories += int(line)

        total_calories = max1+ max2+ max3
        print('top 3 calories sum: ', total_calories)

if __name__=='__main__':
    calculate_part1()
    calculate_part2()