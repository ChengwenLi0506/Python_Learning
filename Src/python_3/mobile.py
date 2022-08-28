import pandas as pd
df = pd.read_excel("mobile.xls",index_col="基站编号")
#print(df.info())
from sklearn.preprocessing import MinMaxScaler
nm = MinMaxScaler(feature_range = (0,1))
val = nm.fit_transform(df.values)
df = pd.DataFrame(data=val, columns=df.columns,index=df.index)
print(df)

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, random_state=1)
kmeans.fit(df)
print(kmeans.cluster_centers_)
df['基站类别'] = kmeans.labels_
print(len(kmeans.labels_))
df.to_excel("mobile2.xls")
