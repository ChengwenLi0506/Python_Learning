import pandas as pd
df = pd.DataFrame(
{

"平台":["京东","淘宝","拼多多","京东","淘宝","拼多多"],
"年份":[2019,2019,2019,2020,2020,2020],
"销量":[100,200,300,400,500,600]
}
)
print(df)

print('-'*100)

# https://blog.csdn.net/Norsaa/article/details/106826729
df1 = pd.pivot(df,index = "年份",columns = "平台",values = "销量")
print(df1)


print('-'*100)
df2 = pd.pivot(df,index = "平台",columns = "年份",values = "销量")
print(df2)