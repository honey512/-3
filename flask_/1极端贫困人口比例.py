from flask import Flask, render_template
import json
import pandas as pd


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

    portion = []
    df1 = df.groupby('location')
    for i in countries:
        portion.append(df1.get_group(i)['extreme_poverty'].iloc[0])

    return name, portion


@app.route("/", methods=["GET"])
def a():
    return render_template('web1.html')

@app.route("/getdata")
def get_data():
    countries, portion = read_data()
    print(countries, portion)
    return json.dumps({'countries': countries, 'portion': portion}, ensure_ascii=False)

if __name__ == '__main__':
    app.run()
