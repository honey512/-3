from flask import Flask, render_template
import json
import pandas as pd
import numpy as np


app = Flask(__name__)

"""统计各洲从2020-3到2022-2的每月新增人数total_cases"""

def read_data():
    """读取文件中的数据"""
    path = 'D:\学习资料\课程设计三\数据\owid-covid-data.csv'
    df = pd.read_csv(path)
    df = df.fillna(0)

    df1 = df.groupby('continent')
    continent = ['Africa', 'Asia', 'Europe', 'North America','Oceania',  'South America']
    dates = ['2020-03-31', '2020-04-30', '2020-05-31', '2020-06-30','2020-07-31', '2020-08-31', '2020-09-30', '2020-10-31',
            '2020-11-30', '2020-12-31', '2021-01-31', '2021-02-28', '2021-03-31', '2021-04-30', '2021-05-31', '2021-06-30',
            '2021-07-31', '2021-08-31', '2021-09-30', '2021-10-31','2021-11-30', '2021-12-31', '2022-01-31', '2022-02-28',]
    cases = []  # 所有洲
    print(len(df1))
    for each1 in df1:
        if each1[1]['continent'].iloc[0] != 0:
            print(each1[1]['continent'].iloc[0])
            one_con = []    # 一个洲
            df2 = each1[1].groupby('location')

            for each2 in df2:
                df3 = each2[1]
                temp = [0]*24   # 一个国家
                for date in df3['date']:
                    if date in dates:
                        temp[dates.index(date)] = float(df3[df3['date'] == date]['total_cases'])

                x = np.array(temp)
                x = np.diff(x)
                one_con.append(x)
                # print(x)
            cases.append([sum(x) for x in zip(*one_con)])

    # for i in continent:
    #     print(df1.get_group(i)['total_cases'],df1.get_group(i)['total_cases'].iloc[-1])
    #     portion.append(df1.get_group(i)['total_cases'].iloc[-1])
    #     # print('国家的数量：--===',i,)

    #
    return continent, dates[1:], cases


@app.route("/", methods=["GET"])
def a():
    return render_template('web2.html')


@app.route("/getdata")
def get_data():
    country, date, case = read_data()
    print(country, date)
    return json.dumps({'country': country, 'date': date, 'case':case}, ensure_ascii=False)

if __name__ == '__main__':
    app.run()
    # read_data()
#     df3 = df1.get_group('France')
#
#     # 取最后一行的月份
#     month = int(df3.iloc[len(df3)-1]['date'][5])
#
#     datas = np.zeros((6, 100))  # 每个国家的新增人数
#     dates = []
#     i = 0
#     for country in countries:
#         df2 = df1.get_group(country)
#         j = 0
#         for date in df2['date']:
#             if (date[:6] == '2021-'+str(month)) or (date[:6] == '2021-'+str(month-1)):
#                 datas[i][j] = (df2[df2['date'] == date]['daily_new_cases'])
#                 if (date not in dates):
#                     dates.append(date)
#                 j += 1
#
#         i += 1
#
#     return datas, dates
#
#
# @app.route("/", methods=["GET"])
# def a():
#     return render_template('web2_new.html')
#
#
# @app.route("/getdata")
# def get_data():
#     country, date = read_data()
#     print(country.tolist(), date)
#     return json.dumps({'country': country.tolist(), 'date': date}, ensure_ascii=False)
#
#
# if __name__ == '__main__':
#     app.run()