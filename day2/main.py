# link - https://adventofcode.com/2022/day/2


def calculate_part1():
    with open('./input.txt', mode='r') as data_file:
        rounds = data_file.readlines()

        rounds_points = 0
        # looping through each round
        for round in rounds:
            opponent, player = round[0], round[2]

            if opponent=='A' and player=='Z':
                rounds_points+= 3
            elif opponent=='A' and player=='Y':
                rounds_points += (6+2)
            elif opponent=='B' and player=='X':
                rounds_points += 1
            elif opponent=='B' and player=='Z':
                rounds_points += (6+3)
            elif opponent=='C' and player=='X':
                rounds_points += (6+1)
            elif opponent=='C' and player=='Y':
                rounds_points+= 2
            else:
                if opponent=='A': rounds_points+= 4
                elif opponent=='B': rounds_points+= 5
                else: rounds_points+= 6
        
        print('points: ', rounds_points)

def calculate_part2():
    game_map = {
        'A': 1,
        'B': 2,
        'C': 3
    }

    with open('./input.txt', mode='r') as data_file:
        rounds = data_file.readlines()
        round_points = 0
        for round in rounds:
            opponent, guess = round[0], round[2]
            if guess == 'Y':
                round_points += (3 + game_map[opponent])
            elif guess == 'X':
                if opponent == 'A':
                    round_points += 3
                elif opponent == 'B':
                    round_points += 1
                else:
                    round_points += 2
            elif guess == 'Z':
                round_points += 6
                if opponent == 'A':
                    round_points += 2
                elif opponent == 'B':
                    round_points += 3
                else:
                    round_points += 1
        
        print('points: ', round_points)


if __name__ == '__main__':
    calculate_part1()
    calculate_part2()