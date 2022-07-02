'''
@coding: utf-8
@author: moyuweiqing
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import pandas as pd

def dySEIDR_G0(y, t, alpha, beta, gamma, delta, lamda):
    """未加政府防控"""
    s, e, i, d, r = y
    n = s + e + i + d + r
    ds_dt = - lamda * beta * s * (i + e) / n
    de_dt = lamda * beta * s * (i + e) / n - alpha * e
    di_dt = alpha * e - gamma * i - delta * i
    dd_dt = delta * i
    dr_dt = gamma * i

    return np.array([ds_dt, de_dt, di_dt, dd_dt, dr_dt])

def dySEIDR_G(y, t, alpha, beta, gamma, delta, lamda):
    """第1天"""
    s, e, i, d, r = y
    n = s + e + i + d + r

    if t >= 1:         # 从第1天开始限制人员接触
        lamda = 2

    ds_dt = - lamda * beta * s * (i + e) / n
    de_dt = lamda * beta * s * (i + e) / n - alpha * e
    di_dt = alpha * e - gamma * i - delta * i
    dd_dt = delta * i
    dr_dt = gamma * i

    return np.array([ds_dt, de_dt, di_dt, dd_dt, dr_dt])

def dySEIDR_G1(y, t, alpha, beta, gamma, delta, lamda):
    """第7天"""
    s, e, i, d, r = y
    n = s + e + i + d + r

    if t >7:         # 从第7天开始限制人员接触
        lamda = 2

    ds_dt = - lamda * beta * s * (i + e) / n
    de_dt = lamda * beta * s * (i + e) / n - alpha * e
    di_dt = alpha * e - gamma * i - delta * i
    dd_dt = delta * i
    dr_dt = gamma * i

    return np.array([ds_dt, de_dt, di_dt, dd_dt, dr_dt])

def dySEIDR_G2(y, t, alpha, beta, gamma, delta, lamda):
    """第14天"""
    s, e, i, d, r = y
    n = s + e + i + d + r

    if t >14:         # 从第14天开始限制人员接触
        lamda = 2

    ds_dt = - lamda * beta * s * (i + e) / n
    de_dt = lamda * beta * s * (i + e) / n - alpha * e
    di_dt = alpha * e - gamma * i - delta * i
    dd_dt = delta * i
    dr_dt = gamma * i

    return np.array([ds_dt, de_dt, di_dt, dd_dt, dr_dt])

def draw_SEIDR(ySEIR0, ySEIR1, ySEIR2, ySEIR3):
    plt.figure(figsize=(16, 9))

    plt.plot(t, ySEIR0[:, 2], '.', label='i0(t)--SEIR')
    plt.plot(t, ySEIR1[:, 2], '--', label='i1(t)--SEIR')
    plt.plot(t, ySEIR2[:, 2], '-.', label='i2(t)--SEIR')
    plt.plot(t, ySEIR3[:, 2], '-', label='i3(t)--SEIR')

    plt.legend()
    # plt.show()
    plt.savefig('./img/' + '5 SEIDR_com_model.jpg')

    # plt.plot(t, ySEIR3[:, 0], '--', label='s(t)--SEIR')
    # plt.plot(t, ySEIR3[:, 1], '-.', label='e(t)--SEIR')
    # plt.plot(t, ySEIR3[:, 2], '-', label='i(t)--SEIR')
    # plt.plot(t, ySEIR3[:, 3], '.', label='d(t)--SEIR')
    # plt.plot(t, ySEIR3[:, 4], '--', label='r(t)--SEIR')
    # plt.legend()
    # # plt.show()
    # plt.savefig('./img/' + '4 SEIDR_G3_model.jpg')

def draw_SEIDR6(ySEIR):
    df = pd.read_csv('China_cases.csv', encoding='utf-8')
    plt.figure(figsize=(16, 9))
    plt.plot(t, ySEIR[:, 3], '--', label='d(t)--SEIR')

    plt.plot(t, df['total_deaths'][10:310], '--', label='total_deaths')
    plt.savefig('./img/' + '6 evaluate.jpg')

# def draw_SEIDR1(ySEIR):
def draw_SEIDR1(ySEIR0, ySEIR1, ySEIR2, ySEIR3):
    import pandas as pd
    import pyecharts.options as opts
    from pyecharts.charts import Line

    df = pd.read_csv('China_cases.csv', encoding='utf-8')
    t = []
    for i in range(300):
        t.append(str(i))

    c = (
        Line()
            .add_xaxis(t)
            # .add_yaxis("total", df['total_deaths'][10:310], is_smooth=True, label_opts=opts.LabelOpts(is_show=False),
            #            markpoint_opts=opts.MarkPointOpts(symbol_size=45,
            #                                              data=[opts.MarkPointItem(name="最大值", type_='max'),
            #                                                    (opts.MarkPointItem(name="最小值", type_='min'))]))
            # .add_yaxis("s(t)--SEIR", ySEIR[:, 0], is_smooth=True, label_opts=opts.LabelOpts(is_show=False),
            #            markpoint_opts=opts.MarkPointOpts(symbol_size=45,
            #                                              data=[opts.MarkPointItem(name="最大值", type_='max'),
            #                                                    (opts.MarkPointItem(name="最小值", type_='min'))]))
            # .add_yaxis("e(t)--SEIR", ySEIR[:, 1], is_smooth=True, label_opts=opts.LabelOpts(is_show=False),
            #            markpoint_opts=opts.MarkPointOpts(symbol_size=45,
            #                                              data=[opts.MarkPointItem(name="最大值", type_='max'),
            #                                                    (opts.MarkPointItem(name="最小值", type_='min'))]))
            # .add_yaxis("i(t)--SEIR", ySEIR[:, 2], is_smooth=True, label_opts=opts.LabelOpts(is_show=False),
            #            markpoint_opts=opts.MarkPointOpts(symbol_size=45,
            #                                              data=[opts.MarkPointItem(name="最大值", type_='max'),
            #                                                    (opts.MarkPointItem(name="最小值", type_='min'))]))
            # .add_yaxis("d(t)--SEIR", ySEIR[:, 3], is_smooth=True, label_opts=opts.LabelOpts(is_show=False),
            #            markpoint_opts=opts.MarkPointOpts(symbol_size=45,
            #                                              data=[opts.MarkPointItem(name="最大值", type_='max'),
            #                                                    (opts.MarkPointItem(name="最小值", type_='min'))]))
            # .add_yaxis("r(t)--SEIR", ySEIR[:, 4], is_smooth=True, label_opts=opts.LabelOpts(is_show=False),
            #            markpoint_opts=opts.MarkPointOpts(symbol_size=45,
            #                                              data=[opts.MarkPointItem(name="最大值", type_='max'),
            #                                                    (opts.MarkPointItem(name="最小值", type_='min'))]))


            .add_yaxis("I(t)--SEIR", ySEIR0[:, 2], is_smooth=True, label_opts=opts.LabelOpts(is_show=False),
                       markpoint_opts=opts.MarkPointOpts(symbol_size=45,
                                                         data=[opts.MarkPointItem(name="最大值", type_='max'),
                                                               (opts.MarkPointItem(name="最小值", type_='min'))]))
            .add_yaxis("I1(t)--SEIR", ySEIR1[:, 2], is_smooth=True, label_opts=opts.LabelOpts(is_show=False),
                       markpoint_opts=opts.MarkPointOpts(symbol_size=45,
                                                         data=[opts.MarkPointItem(name="最大值", type_='max'),
                                                               (opts.MarkPointItem(name="最小值", type_='min'))]))
            .add_yaxis("I2(t)--SEIR", ySEIR2[:, 2], is_smooth=True, label_opts=opts.LabelOpts(is_show=False),
                       markpoint_opts=opts.MarkPointOpts(symbol_size=45,
                                                         data=[opts.MarkPointItem(name="最大值", type_='max'),
                                                               (opts.MarkPointItem(name="最小值", type_='min'))]))
            .add_yaxis("I3(t)--SEIR", ySEIR3[:, 2], is_smooth=True, label_opts=opts.LabelOpts(is_show=False),
                       markpoint_opts=opts.MarkPointOpts(symbol_size=45,
                                                         data=[opts.MarkPointItem(name="最大值", type_='max'),
                                                               (opts.MarkPointItem(name="最小值", type_='min'))]))


            .set_global_opts(
            title_opts=opts.TitleOpts(title="SEIR"),
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value} %"),
                                     splitline_opts=opts.SplitLineOpts(is_show=True), ),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        )
            .render("pre.html")
    )


if __name__ == '__main__':
    number = 1444216102  # 模型总人数

    s = 17988  # 现存易感人群数量
    e = 4562  # 现存潜伏者
    i = 2088  # 现存感染者
    d = 259  # 累计死亡者
    r = 250  # 累计康复者

    alpha = 0.045  # 潜伏期的人变成感染者的概率
    beta = 0.05  # 对于易感者，与感染者接触后成为潜伏者的可能性
    gamma = 0.08  # 感染者的治愈率
    delta = 0.022  # 感染者的死亡率
    lamda = 5  # 单位时间内感染者接触的人数

    tEnd = 300  # 300天
    t = np.arange(0, tEnd, 1)

    Y0 = (s, e, i, d, r)
    # ySEIR = odeint(dySEIDR_G, Y0, t, args=(alpha, beta, gamma, delta, lamda))
    # draw_SEIDR(ySEIR)
    # draw_SEIDR1(ySEIR)
    ySEIR0 = odeint(dySEIDR_G0, Y0, t, args=(alpha, beta, gamma, delta, lamda))
    ySEIR1 = odeint(dySEIDR_G, Y0, t, args=(alpha, beta, gamma, delta, lamda))
    ySEIR2= odeint(dySEIDR_G1, Y0, t, args=(alpha, beta, gamma, delta, lamda))
    ySEIR3 = odeint(dySEIDR_G2, Y0, t, args=(alpha, beta, gamma, delta, lamda))

    # draw_SEIDR(ySEIR0,ySEIR1, ySEIR2, ySEIR3)
    draw_SEIDR6(ySEIR0)
    # draw_SEIDR1(ySEIR0,ySEIR1, ySEIR2, ySEIR3)
