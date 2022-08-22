from pyecharts.charts import *
from pyecharts.commons.utils import JsCode
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line
import pandas as pd

df = pd.read_excel("byd_sales.xlsx", sheet_name= '2021')
df2022 = pd.read_excel("byd_sales.xlsx", sheet_name= '2022')
print(df)

#df2022.dropna(axis=0, how='any', inplace=True);
print(df2022)


#2021 sheet
data = df.values

#2022sheet
data2 = df2022.values

#2021 销量列
sell21 = df['销量'].values.tolist()

#2022 销量列
sell22 = df2022['销量'].values.tolist()

#同比增长率
linedata = ((df2022['销量'].values - df['销量'].values) / df['销量'].values).tolist()
print(linedata)

linedata1 = [round(n, 3)*100 for n in linedata]
print(linedata1)

#for i in range(0, len(linedata)):
    #linedata[i] = "%.1f%%"%(linedata[i]),
#print(linedata,type(linedata))

#x轴
x_data = ["{}月".format(i) for i in range(1, 8)]
bar = (
    Bar()
    .set_global_opts(
        title_opts=opts.TitleOpts(title="2021-2022 年销量数据同比", pos_left='center',title_textstyle_opts=opts.TextStyleOpts(color='#FFFFFF',font_weight='bold', font_size=30)),
        legend_opts=opts.LegendOpts(pos_top='bottom'),
        xaxis_opts=opts.AxisOpts(axistick_opts=opts.AxisTickOpts(is_show=False),axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color='#FFFFFF'))),
        yaxis_opts=opts.AxisOpts(
            is_show=False,
            axisline_opts=opts.AxisLineOpts(is_show=False),
            axistick_opts=opts.AxisTickOpts(is_show=False)
        )
    )
    .add_xaxis(x_data)
    #每年销量柱状图
    .add_yaxis(
        "2021年",
        sell21,
        yaxis_index=0,
        color="#5793f3",
        label_opts=opts.LabelOpts(is_show=True,color='#FFFFFF'),
    )
    .add_yaxis(
        "2022年",
        sell22,
        yaxis_index=0,
        color="#87CEEB",
        label_opts=opts.LabelOpts(is_show=True,color='#FFFFFF'),
    )
    #右边刻度
    .extend_axis(
        yaxis=opts.AxisOpts(
            type_="value",
            min_=0,
            max_=350,
            position="right",
            split_number = 7,
            axisline_opts=opts.AxisLineOpts(is_show=False),
            axistick_opts=opts.AxisTickOpts(is_show=False),
            axislabel_opts=opts.LabelOpts(color='#FFFFFF',formatter="{value}%"),
        )
    )
    #左边刻度
    .extend_axis(
        yaxis=opts.AxisOpts(
            min_=0,
            max_=180000,
            position="left",
            grid_index = 0,
            split_number = 9,
            interval = 20000,
            axisline_opts=opts.AxisLineOpts(is_show=False),
            axistick_opts=opts.AxisTickOpts(is_show=False),
            axislabel_opts=opts.LabelOpts(color='#FFFFFF'),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        )
    )
)
#同比增长率折线
line = (
    Line()
    .add_xaxis(x_data)
    .add_yaxis(
        "同比增长率",
        linedata1,
        linestyle_opts=opts.LineStyleOpts(color='#87CEFA',width=4),
        yaxis_index=1,
        label_opts=opts.LabelOpts(color='#FFFFFF',formatter=JsCode("function (params) {return params.value[1] + '%'}")),
    )
    # 右边刻度
    .extend_axis(
        yaxis=opts.AxisOpts(
            type_="value",
            min_=0,
            max_=350,
            position="right",
            split_number=7,
            axisline_opts=opts.AxisLineOpts(is_show=False),
            axistick_opts=opts.AxisTickOpts(is_show=False),
            axislabel_opts=opts.LabelOpts(color='#FFFFFF', formatter="{value}%"),
        )
    )
)

bar.overlap(line)
# line.overlap(bar)

grid = Grid()
grid.bg_color = "#808080"
grid.add(bar, opts.GridOpts(pos_left="20%", pos_right="20%"), is_control_axis_index=True)
grid.render("grid_multi_yaxis.html")

