from collections import deque

class Module:
    def __init__(self, tag, type, receivers, memory):
        self.tag = tag
        self.type = type
        self.receivers = receivers
        self.memory = memory
        
    def __str__(self):
        return f"Module(tag={self.tag}, type={self.type}, receivers={self.receivers}, memory={self.memory})"

with open('input.txt') as text_input:
    modules = {}

    for line in text_input.read().splitlines():
        description, receivers_str = line.split(' -> ')
        receivers = receivers_str.split(', ')

        if description == 'broadcaster':
            tag = description
            modules[tag] = Module(tag, 'broadcaster', receivers, {})
        else:
            tag = description[1:]
            modules[tag] = Module(tag, description[0], receivers, {})
    
    for module in modules.values():
        for receiver in module.receivers:
            if receiver in modules:
                modules[receiver].memory[module.tag] = False

    clusters = [('sj', 'vd'), ('vn', 'nd'),('tg', 'tx'),('kn', 'pc')]

    for start, end in clusters:
        stop = False
        button_press = 0

        while not stop:
            # _ = input('Press the button')
            pulses = deque([('broadcaster', False, start)])
            button_press += 1       

            while pulses:
                sender, state, receiver = pulses.popleft()
                # print(f'{sender} -{['low', 'high'][state]}-> {receiver}')

                if receiver == end and not state:
                    stop = True
                    break

                if receiver not in modules:
                    continue

                module = modules[receiver]

                if module.tag == 'broadcaster':
                    for next_receiver in module.receivers:
                        pulses.append((module.tag, state, next_receiver))
                else:                
                    if module.type == '%':
                        if state:
                            continue
                        module.memory['global'] = not module.memory.get('global', False)
                    
                    if module.type == '&':
                        module.memory[sender] = state

                    for next_receiver in module.receivers:
                        if module.type == '%':
                            pulses.append((module.tag, module.memory['global'], next_receiver))
                        
                        if module.type == '&':
                            conjunction = not all(module.memory.values())
                            pulses.append((module.tag, conjunction, next_receiver))

        print(button_press)
