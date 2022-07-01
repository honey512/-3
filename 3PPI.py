"""中国工业品出口价格指数数据"""

import pandas as pd


import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker

df = pd.read_csv('D:\学习资料\课程设计三\数据\gmjj\\PPI.csv')
date = []
ppi = []
per = []

for i in range(len(df)-1, -1, -1):
    data = df.iloc[i]
    print(data['Month'][:5])
    if data['Month'][:4] == '2019' or data['Month'][:4] == '2020' or data['Month'][:4] == '2021':
        date.append(data['Month'])
        ppi.append(data['Curent_Month'])
        per.append(data['Curent_Month_YOY'][:-1])

print(per)

# c = (
#     Line()
#     .add_xaxis(date)
#     .add_yaxis("商家A", ppi, is_smooth=True, )
#     .set_global_opts(title_opts=opts.TitleOpts(title="Line-smooth"))
#     .render("PPI.html")
# )

from pyecharts import options as opts
from pyecharts.charts import Bar, Line



bar = (
    Bar()
    .add_xaxis(date)
    .add_yaxis("当月同比增长", per,category_gap=10, )
    .extend_axis(
        yaxis=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(formatter="{value}"),
            interval=3,
            is_scale=True,  # 坐标轴不从0开始
            splitline_opts=opts.SplitLineOpts(is_show=True),    # 显示网格
        )
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="PPI"),
        yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value} %")),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross")
    )

)

line = Line().add_xaxis(date).add_yaxis("当月", ppi, yaxis_index=1, is_smooth=True)
bar.overlap(line)
bar.render("PPI.html")



