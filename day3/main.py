# link - https://adventofcode.com/2022/day/3


def calculate_part1():
    with open('./input.txt', mode='r') as data_file:
        racks = data_file.readlines()
        priority_sum = 0
        for rack in racks:            
            final = set()
            right, left = len(rack)-1, 0
            first_half = set(rack[0:len(rack)//2])
            second_half = set(rack[len(rack)//2: len(rack)])
            while (left<right):
                if rack[left] in second_half:
                    if rack[left] not in final:
                        if rack[left]>='a' and rack[left]<='z':
                            priority_sum += (ord(rack[left]) - ord('a')+ 1)
                        else:
                            priority_sum += (ord(rack[left]) - ord('A')+ 27)
                    final.add(rack[left])

                if rack[right] in first_half:
                    if rack[right] not in final:
                        if rack[right]>='a' and rack[right]<='z':
                            priority_sum += (ord(rack[right]) - ord('a')+ 1)
                        else:
                            priority_sum += (ord(rack[right]) - ord('A')+ 27)
                    final.add(rack[right])
                left+= 1
                right-=1    
        print('final points: ', priority_sum)

def calculate_part2():
    with open('./input.txt', mode='r') as data_file:
        racks = data_file.readlines()
        racks_len = len(racks)
        priority_sum = 0
        for index in range(0, racks_len, 3):
            set1, set2, set3 = set(racks[index]), set(racks[index+1]), set(racks[index+2])
            common = set1 & set2 & set3
            for ele in common:
                if ele>='a' and ele<='z':
                    priority_sum += (ord(ele)-ord('a')+1)
                elif ele>='A' and ele<='Z':
                    priority_sum += (ord(ele)-ord('A')+27)
        print('part2 priorit sum: ', priority_sum)

if __name__ == '__main__':
    calculate_part1()
    calculate_part2()