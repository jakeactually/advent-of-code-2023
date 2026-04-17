import re

digits_regex = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'

digits_mapping = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

with open('input.txt') as input:
    sum = 0

    for line in input:
        digits = re.findall(digits_regex, line)
        # print(digits)
        parsed = [digits_mapping.get(digit, digit) for digit in digits]
        # print(parsed)
        sum += int(parsed[0] + parsed[-1])
        # print(sum)

    print(sum)
