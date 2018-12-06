import pandas as pd
import numpy as np

data = pd.read_csv('day_4.txt', header =None)
data.columns = ['text']

data['action'] = data.text.apply(lambda x : x.split('] ')[1] )
data['time'] = data.text.apply(lambda x : x.split('] ')[0] )
data['date'] = data.time.apply(lambda x: x.split(' ')[0][1:].split('1518-')[1])
data['time'] = data.time.apply(lambda x: x.split(' ')[1])

data = data[['date','time','action']]
data = data.sort_values(['date','time']).reset_index()

sleepTime = {}

guard = -1
times= []
for index, row in data.iterrows():
    if 'Guard' in row.action:
        if guard in sleepTime.keys():
            sleepTime[guard].append(times)
        else:
            sleepTime[guard] = [ times]
        times = []
        guard = row.action.split('#')[1].split(' begins')[0]
    if 'asleep' in row.action:
        times.append( row.time )
    if 'wakes' in row.action:
        times.append( row.time )

sleepers = {}
for guard, shifts in sleepTime.items():

    totalSleep = 0
    for shift in shifts:
        times = np.array([ int(x.split(':')[1]) for x in shift])
        mask = np.ones(times.shape)
        mask[1::2] = -1
        totalSleep += -sum(times * mask)
    sleepers = { 'guard' : guard, 'sleepTime':totalSleep}