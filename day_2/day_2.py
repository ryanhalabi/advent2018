import pandas as pd
import numpy as np

data = pd.read_csv('day_2_1_input.txt', header =None)
data.columns = ['id']

def checkList(l, store):

    if len(l) == 0:
        return store
        
    if len(store) == 2:
        return store

    target = l[0]

    c = len([x for x in l if x == target])
    if c in [2,3]:
        store.append(c)
        store = list(set(store))

    newList = [x for x in l if x != target]
    store = checkList( newList,store)
    return store


# data['ids'] = data.id.apply( lambda x : checkList(x,[]))  
# data['two'] = data.ids.apply( lambda x : int(2 in x)) 
# data['three'] = data.ids.apply( lambda x : int(3 in x)) 

# data.loc[0,'id'] = 'abcdef'
# data.loc[1,'id'] = 'abcdeg'
# data = data.iloc[0:2]

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

