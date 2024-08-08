import pandas as pd
from functools import reduce
Data={
    'Numbers':[1,2,3,4,5],
    'Letters':['A','B','C','D','E']
}
df=pd.DataFrame(Data)
sq=df['Numbers'].map(lambda x:x**2)
ev=list(filter(lambda x:x%20,df['Numbers']))
po=reduce(lambda x,y:x*y,df['Numbers'])
print("Dataframe:\n",df)
print("map for squaring:\n",sq)
print("reducing for product:\n",po)