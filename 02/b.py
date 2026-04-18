import re

head_regex = r'Game (\d+)'
set_regex = r'(\d+) (red|green|blue)'

def set_is_valid(amount, color):
    match color:
        case 'red':
            return int(amount) <= 12
        case 'green':
            return int(amount) <= 13
        case 'blue':
            return int(amount) <= 14

with open('input.txt') as input:
    total = 0

    for line in input:
        game_id = re.findall(head_regex, line)
        sets = re.findall(set_regex, line)

        valid = all(
            set_is_valid(amount, color) for amount, color in sets
        )

        if valid:
            total += int(game_id[0])

    print(total)
