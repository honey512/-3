"""制造业同比增长和非制造业同比增长"""
import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker

df = pd.read_csv('D:\学习资料\课程设计三\数据\gmjj\\PMI.csv')
date = []
pro = []
non_pro = []

for i in range(len(df)-1, -1, -1):
    data = df.iloc[i]
    print(data['Montth'][:5])
    if data['Montth'][:4] == '2019' or data['Montth'][:4] == '2020' or data['Montth'][:4] == '2021' or data['Montth'][:4] == '2022':
        date.append(data['Montth'][:-1])
        pro.append(data['Manufacturing_YOY'][:-1])
        non_pro.append(data['Nonmanufacturing_YOY'][:-1])

print(pro)

c = (
    Line()
    .add_xaxis(date)
    .add_yaxis("制造业同比增长", pro, is_smooth=True,label_opts=opts.LabelOpts(is_show=False),
                markpoint_opts=opts.MarkPointOpts(symbol_size=45,data=[opts.MarkPointItem(name="最大值", type_='max'),
                                                        (opts.MarkPointItem(name="最小值", type_='min'))]))
    .add_yaxis("非制造业同比增长", non_pro, is_smooth=True,label_opts=opts.LabelOpts(is_show=False),
               markpoint_opts=opts.MarkPointOpts(symbol_size=45, data=[opts.MarkPointItem(name="最大值", type_='max'),
                                                                      (opts.MarkPointItem(name="最小值", type_='min'))]))

    .set_global_opts(
        title_opts=opts.TitleOpts(title="PMI"),
        yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value} %"),
                                 splitline_opts=opts.SplitLineOpts(is_show=True),),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
    )
    .render("PMI.html")
)
