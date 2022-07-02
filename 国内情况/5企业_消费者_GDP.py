"""2018~2021年企业家和消费者信心对经济增长的影响研究——基于对企业家信心指数和消费者信心指数的分析"""
"""制造业同比增长和非制造业同比增长"""
import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker

df = pd.read_csv('D:\学习资料\课程设计三\数据\gmjj\\Enterprise_Confidence.csv')
date = []
econ = []
CCI = [119.83,
       118.83,
       122.03,
       124,
       122.6,
       118.03,
       114.93,
       122.5,
       125.16,
       123.63,
       124.86,
       125.76,124.63,122.1,124.6,126.26]
#
for i in range(len(df) - 1, -1, -1):
    data = df.iloc[i]
    print(data['Quarter'][:5])
    if data['Quarter'][:4] == '2019' or data['Quarter'][:4] == '2020' or data['Quarter'][:4] == '2021' or data[
                                                                                                              'Quarter'][
                                                                                                          :4] == '2018':
        date.append(data['Quarter'])
        econ.append(data['Macro_econ_Climate_Index'])

df1 = pd.read_csv('D:\学习资料\课程设计三\数据\gmjj\\GDP.csv')
GDP = []
for i in range(len(df1) - 1, -1, -1):
    data = df1.iloc[i]
    print(data['Quater'][:5])
    if data['Quater'][:4] == '2019' or data['Quater'][:4] == '2020' or data['Quater'][:4] == '2021' or data[
                                                                                                              'Quater'][
                                                                                                          :4] == '2018':
        GDP.append(data['GDP_YOY'][:-1])

print(econ)

c = (
    Line()
        .add_xaxis(date)
        .add_yaxis("企业家信心指数", econ, is_smooth=True, label_opts=opts.LabelOpts(is_show=False),
                   markpoint_opts=opts.MarkPointOpts(symbol_size=45, data=[opts.MarkPointItem(name="最大值", type_='max'),
                                                                           (opts.MarkPointItem(name="最小值",
                                                                                               type_='min'))]))
        .add_yaxis("消费者信心指数", CCI, is_smooth=True,label_opts=opts.LabelOpts(is_show=False),
                   markpoint_opts=opts.MarkPointOpts(symbol_size=45, data=[opts.MarkPointItem(name="最大值", type_='max'),
                                                                          (opts.MarkPointItem(name="最小值", type_='min'))]))
        .extend_axis(
                yaxis=opts.AxisOpts(
                    axislabel_opts=opts.LabelOpts(formatter="{value} %"),
                    is_scale=True,  # 坐标轴不从0开始
                    splitline_opts=opts.SplitLineOpts(is_show=True),    # 显示网格
                )
            )
        .set_global_opts(
        title_opts=opts.TitleOpts(title="企业家-消费者信心指数"),
        yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value}"),),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
    )
)
line = Line().add_xaxis(date).add_yaxis("国内生产总值同比增长", GDP, yaxis_index=1, is_smooth=True)
c.overlap(line)
c.render("ECG.html")
