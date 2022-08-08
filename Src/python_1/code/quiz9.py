
import numpy as np
import pandas as pd

d={'M':[0,4,8,12],'N':[1,5,9,13],'O':[2,6,10,14],'P':[3,7,11,15]}

print(type(d))
print(d)
print('-'*100)

#dict to DataFrame
df = pd.DataFrame(data=d,index=list('abcd'))

print(type(df))
print(df)
print('-'*100)


#DataFrame to dict
v=df.to_dict(orient='list')

print(type(v))
print(v)
print('-'*100)



