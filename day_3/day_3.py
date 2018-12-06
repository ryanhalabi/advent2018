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

data['mat'] = data.id.apply( lambda x : np.zeros([1000,1000]) ) 

total = data.mat.sum()

sum(sum(total>1))

data['overlap'] = data.apply( lambda row, total = total : total[ row.x:row.x +row.w, row.y:row.y + row.h].max()>1  , axis=1)