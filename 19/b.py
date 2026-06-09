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

    for part in parts:
        current_flow_key = 'in'
        complete = False

        x = part['x']
        m = part['m']
        a = part['a']
        s = part['s']

        while not complete:
            current_flow = flows.get(current_flow_key, [current_flow_key])

            for step in current_flow:
                if step == 'A':
                    accepted_parts.append(part)
                    complete = True
                    break

                if step == 'R':
                    complete = True
                    break

                if ':' not in step:
                    current_flow_key = step
                    break

                exp, next_flow_key = step.split(':')

                if eval(exp):
                    current_flow_key = next_flow_key
                    break

    total = 0

    for part in accepted_parts:
        for value in part.values():
            total += value

    print(total)
