import pandas as pd

x = pd.read_csv('day_1_1_input.txt', header = None)
x.columns = ['int']
x['csum'] = x.cumsum()

past = x.copy()
past['ind'] = past.index
past['f'] = past.csum.apply( lambda y : past[past.csum == y].ind.iloc[0]).astype(int)

matches = pd.DataFrame()
i=0
while matches.size == 0:
    print(i)
    last = past.csum.iloc[-1]
    new = x.copy()
    new.csum += last

    new['ind'] = new.index + past.shape[0]

    current = pd.concat([past,new],ignore_index=True, sort=False)
    current.loc[ new.ind,'f'] = new.csum.apply( lambda y : current[current.csum == y].ind.iloc[0].astype(int) ).values

    matches = current[ current.ind != current.f]
    past = current
    i+=1

print(matches)