import pandas as pd
import numpy as np

data = pd.read_csv('day_3.txt', header =None)

data['id'] = data[0].apply( lambda x : x.split(' @ ')[0] )
data['x'] = data[0].apply( lambda x : x.split(' @ ')[1] ).astype(int)
data['y'] = data[1].apply( lambda x : x.split(': ')[0] ).astype(int)
data['w'] = data[1].apply( lambda x : x.split(': ')[1].split('x')[0] ).astype(int)
data['h'] = data[1].apply( lambda x : x.split(': ')[1].split('x')[1] ).astype(int)
data['all'] = data[0] + data[1]

data = data[ ['all','id','x','y','w','h']]

data['max_x'] = data.x + data.w
data['max_y'] = data.y + data.h

data['mat'] = 0

data['mat'] = data.id.apply( lambda x : np.zeros([data.max_x.max(), data.max_y.max()]) )

def makeMat(row):
    mat = row.mat
    mat[ row.x:row.x+row.w, row.y:row.y+row.h] = 1
    return mat


data.mat = data.apply( lambda row : makeMat(row) )




data['nl'] = data.id.apply( lambda x : np.array([ ord(char) - 96 for char in x ]))

for index,row in data.iterrows():
    print(index)
    target = row.nl
    source = data.iloc[index+1:].copy()
    source['dif'] = source.nl.apply( lambda x :np.abs( x - target) ) 

    source['win'] = source.dif.apply( lambda x : len([ y for y in x if y != 0]) == 1 )

    if source.win.sum()>0:
        print('yay')
        break

winner = source[source.win].dif.iloc[0]
winner = 1 - winner/max(winner)

wintext = ''.join( [x for x in row.id if x in winner] )

source[source.win].iloc[0].id[0:15] + source[source.win].iloc[0].id[16:]

