def invert_cond_and_limit(cond, limit):
    if cond[1] == '>':
        return (cond[0] + '<', limit + 1)
    else:
        return (cond[0] + '>', limit - 1)

def before_or_after(cond, before, after):
    if '>' in cond:
        return max(before, after)
    else:
        return min(before, after)

with open('input.txt') as input:
    flows_text, parts_text = input.read().split('\n\n')
    flows = {}

    for line in flows_text.splitlines():
        part_key, part_values_string = line[:-1].split('{')
        part_values = part_values_string.split(',')
        flows[part_key] = part_values

    parts = []

    for line in parts_text.splitlines():
        part = {}

        for value in line[1:-1].split(','):
            key, val = value.split('=')
            part[key] = int(val)
        
        parts.append(part)

    accepted_parts = []

    pending_parts = [{
        'current_flow_key': 'in',
        'current_flow_index': 0,
        'x>': 0,
        'x<': 4001,
        'm>': 0,
        'm<': 4001,
        'a>': 0,
        'a<': 4001,
        's>': 0,
        's<': 4001,
    }]

    while pending_parts:
        for p in pending_parts:
            print(p)
        print()

        current_part = pending_parts.pop()       
        current_flow_key = current_part['current_flow_key']
        current_flow = flows[current_flow_key]
        step = current_flow[current_part['current_flow_index']]

        if step == 'A':
            accepted_parts.append(current_part)
            continue

        if step == 'R':
            continue

        if ':' not in step:
            positive = current_part.copy()
            positive['current_flow_key'] = step
            positive['current_flow_index'] = 0
            pending_parts.append(positive)
            continue

        exp, next_flow_key = step.split(':')
        cond = exp[:2]
        limit = int(exp[2:])

        positive = current_part.copy()

        if next_flow_key != 'R':
            positive[cond] = before_or_after(cond, positive[cond], limit)

            if next_flow_key == 'A':
                accepted_parts.append(positive)
            else:
                positive['current_flow_key'] = next_flow_key
                positive['current_flow_index'] = 0
                pending_parts.append(positive)

        negative = current_part.copy()
        next_cond, next_limit = invert_cond_and_limit(cond, limit)
        negative[next_cond] = before_or_after(next_cond, negative[next_cond], next_limit)
        negative['current_flow_index'] += 1
        pending_parts.append(negative)

    total = 0

    for p in accepted_parts:
        print(p)
        product = 1

        for c in 'xmas':
            mult = p[c + '<'] - p[c + '>'] - 1
            print(c, mult)
            product *= mult

        print('product', product)
        total += product

    print('total', total)