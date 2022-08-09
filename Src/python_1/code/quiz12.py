import pandas as pd


df = pd.DataFrame(
    {
        "平台":["京东","淘宝","拼多多","京东","淘宝","拼多多"],
        "年份":[2019,2019,2019,2020,2020,2020],
        "销量":[100,200,300,400,500,600]
    }
)

print(df)
print(type(df))
print('-'*100)
print(df.info())


print('-'*100)

# 透视图，是由一个DataFrame，重新根据index, columns values生成一张新的DataFrame
# https://blog.csdn.net/Norsaa/article/details/106826729
df1 = pd.pivot(df,index = "年份",columns = "平台",values = "销量")
print(df1)
print(df1.info())

print('-'*100)
# 透视图，是由一个DataFrame，重新根据index, columns values生成一张新的DataFrame
# https://blog.csdn.net/Norsaa/article/details/106826729
df2 = pd.pivot(df,index = "平台",columns = "年份",values = "销量")
print(df2)
print(df2.info())


