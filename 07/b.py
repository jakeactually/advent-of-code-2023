import re

card_ranks = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

five_of_a_kind = re.compile(r'(\w)\1{4}')
four_of_a_kind = re.compile(r'(\w)\1{3}')
full_house = re.compile(r'(\w)\1{2}(\w)\2|(\w)\3(\w)\4{2}')
three_of_a_kind = re.compile(r'(\w)\1{2}')
two_pairs = re.compile(r'(\w)\1.*(\w)\2')
one_pair = re.compile(r'(\w)\1')

patterns = [
    five_of_a_kind,
    four_of_a_kind,
    full_house,
    three_of_a_kind,
    two_pairs,
    one_pair
]

def hand_rank(hand):
    sorted_hand = ''.join(sorted(hand))
    scores = [card_ranks[card] for card in hand]

    for i, pattern in enumerate(patterns):
        if pattern.search(sorted_hand):
            return [7 - i] + scores
    
    return [1, *scores]

with open('input.txt') as input:
    lines = input.read().splitlines()
    cards_bids = [line.split() for line in lines]
    sorted_cards_bids = sorted(cards_bids, key=lambda x: hand_rank(x[0]))
    total = sum(int(bid) * i for i, (_, bid) in enumerate(sorted_cards_bids, start=1))
    print(total)
