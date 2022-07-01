from flask import Flask, render_template
import json
import pandas as pd
import numpy as np


app = Flask(__name__)

"""统计发达国家、发展中国家、不发达国家的extreme_poverty
    (生活在极端贫困中的人口比例，自 2010 年以来)"""

def read_data():
    """读取文件中的数据"""
    path = 'D:\学习资料\课程设计三\数据\owid-covid-data.csv'
    df = pd.read_csv(path)
    countries = ['Italy', 'Spain', 'Canada', 'Portugal', 'South Korea',
                 'China', 'Russia', 'India', 'Malaysia', 'Brazil',
                 'Bangladesh', 'Myanmar', 'Ethiopia', 'Niger', 'Benin']
    name = ['意大利', '西班牙', '加拿大', '葡萄牙', '韩国',
                 '中国', '俄罗斯', '印度', '马来西亚', '巴西',
                 '孟加拉', '缅甸', '埃塞俄比亚', '尼日尔', '贝宁']

    death = []
    total = []
    hospital = []
    df1 = df.groupby('location')
    for i in countries:
        death.append(df1.get_group(i)['total_deaths_per_million'].iloc[-1])
        total.append(df1.get_group(i)['total_cases'].iloc[-1])
        hospital.append(df1.get_group(i)['hospital_beds_per_thousand'].iloc[-1])
    print(death)
    print(total)
    # print(np.array(death)/np.array(total)*100)
    print(hospital)

    return name, death, total, hospital


@app.route("/", methods=["GET"])
def a():
    return render_template('web6.html')

@app.route("/getdata")
def get_data():
    countries, death, total, hospital = read_data()
    return json.dumps({'countries': countries, 'death': death, 'total':total, 'hospital':hospital}, ensure_ascii=False)

if __name__ == '__main__':
    app.run()
    # read_data()