import pandas as pd

with open('input.txt') as input:
    time_distance = pd.read_table(input, index_col=0, header=None, sep=r'\s+')

    for label, content in time_distance.items():
        time = content['Time:']
        distance = content['Distance:']

        for i in range(time):
            if i * (time - i) > distance:
                print(time + 1 - i * 2)
                break
