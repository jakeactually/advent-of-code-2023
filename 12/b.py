class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def list_to_linked_list(items):
    if not items:
        return None

    head = Node(items[0])
    current = head

    for value in items[1:]:
        current.next = Node(value)
        current = current.next

    return head

with open('input.txt') as input:
    total = 0

    for line in input:
        [springs, counts] = line.strip().split(' ')
        list_springs = list_to_linked_list(([*springs, '?'] * 5)[:-1])
        int_counts = [int(i) for i in counts.split(',')] * 5
        
        stack = [([], False, list_springs)]
        result = []

        def stack_append(tuple):
            # print(tuple)
            stack.append(tuple)

        while stack:
            (groups, in_group, springs) = stack.pop()

            if not springs:
                if groups == int_counts:
                    result.append(groups)
                continue

            x = springs.value
            xs = springs.next

            match x:
                case '?':
                    a = Node('#')
                    a.next = xs
                    b = Node('.')
                    b.next = xs
                    stack.append((groups, in_group, a))
                    stack.append((groups.copy(), in_group, b))
                case '#':
                    if not in_group:
                        groups.append(0)
                    group_index = len(groups) - 1
                    groups[group_index] += 1
                    if group_index < len(int_counts) and groups[group_index] <= int_counts[group_index]:
                        stack.append((groups, True, xs))
                case '.':
                    if in_group:
                        group_index = len(groups) - 1
                        if groups[group_index] == int_counts[group_index]:
                            stack.append((groups, False, xs))
                    else:
                        stack.append((groups, False, xs))
        
        print(len(result))
        total += len(result)

    print(total)
