'''
黄红梅
2022-6-21
本文件用于数据处理及画图
'''
import os
import jieba
# import wordcloud
import chardet
import imageio


import jieba.analyse
import pandas as pd
import matplotlib.pyplot as plt
from gensim.corpora import Dictionary
import jieba.posseg as pseg
# def zhexian():
from gensim import models
def t1():
    df = pd.read_csv('gmjj/CPGI.csv')
    df = df.reindex(index=df.index[::-1])
    l = range(2005,2023)
    lab = []
    for i in l:
        df1 = df[df['Month'].str.contains(str(i))]
        print(df1)
        # plt.plot(range(1,len(df1)+1),df1['CPGI'])
        lab.append(str(i))
        half = 2010
        half2=2017#币值稳定状况的价格指数指标
        if i < half:
            plt.figure('第一个图片币值稳定状况')
            plt.plot(range(1,len(df1)+1), df1['CPGI'],label=str(i))
            plt.legend()
        else:
            if i>half and i<half2:
                plt.figure('第二个图片币值稳定状况')
                plt.plot(range(1,len(df1)+1), df1['CPGI'],label=str(i))
                plt.legend()
            else:
                plt.figure('第三个图片币值稳定状况')
                plt.plot(range(1, len(df1) + 1), df1['CPGI'], label=str(i))
                plt.legend()

    # plt.legend(lab, loc='upper right', bbox_to_anchor=(1.2, 1))
    plt.show()

def t2():
    df = pd.read_csv('gmjj/RSCG.csv')
    df = df.reindex(index=df.index[::-1])
    l = range(2008,2022)
    lab = []
    for i in l:
        df1 = df[df['Month'].str.contains(str(i))]
        print(df1)
        df1['Total_YOY'] = df[u'Total_YOY'].str.strip('%').astype(float)
        # plt.plot(range(1,len(df1)+1),df1['CPGI'])
        lab.append(str(i))
        half = 2015
        half2=2017#中国社会消费品零售总额增长率数据
        if i < half:
            plt.figure('第一个图片中国社会消费品零售总额增长率数据')
            plt.plot(range(1,len(df1)+1), df1['Total_YOY'],label=str(i))
            plt.legend()
        else:
            # if i>half and i<half2:
            #     plt.figure('第二个图片中国社会消费品零售总额数据')
            #     plt.plot(range(1,len(df1)+1), df1['Total_YOY'],label=str(i))
            #     plt.legend()
            # else:
                plt.figure('第三个图片中国社会消费品零售总额增长率数据')
                plt.plot(range(1, len(df1) + 1), df1['Total_YOY'], label=str(i))
                plt.legend()

    # plt.legend(lab, loc='upper right', bbox_to_anchor=(1.2, 1))
    plt.show()
def open_file(path,a):
    decode_set = ['gbk', 'utf-8', 'gd18030', 'ISO-8859-2', 'gb2312', 'Error']
    for k in decode_set:
        try:
            file = open(path+'/'+a, 'r', encoding=k)
            readfile = file.read()
            file.close()
            return readfile
        except:
            if k == 'Error':
                print('errro')
                raise Exception("%s had no way to decode" % path)
            continue
def t3():
    path='china_policy'
    df = pd.DataFrame()
    ll=[]
    stopwords = {line.strip(): 1 for line in open('cn_stopwords.txt', 'r', encoding='utf-8').readlines()}
    for i,j,k in os.walk(path):
        path2 = i
        list1 =''
        print(path2,len(k))
        for a in k:
            f = open_file(path2,a)
            word = [w.word for w in pseg.cut(f) if w.word not in stopwords]
            # print(word)
            list1=list1+''.join(word)
        # l = str.replace('.', '').replace(',', '').replace('\n', '').replace('(', '').replace(')', '').replace(':','').replace('—', '').replace('[','').replace(']','').replace('!','')  # 将文件中的符号替代
        # list1 = l.split()
        if len(list1)==0:
            continue
        keywords_textrank = jieba.analyse.textrank(list1, withWeight=True)
        # df2 = pd.DataFrame()
        # df2['word'] = [list1]
        # ll.append(keywords_textrank)
        df2 = pd.DataFrame()
        print(keywords_textrank)
        first, snd = zip(*keywords_textrank)
        df2['year'] = [i[-6:]]*len(keywords_textrank)
        df2['name'] = first
        df2['fan_num'] = snd

        df = df.append(df2)

        # stopwords = {line.strip(): 1 for line in open('cn_stopwords.txt', 'r', encoding='utf-8').readlines()}
        # words = []
        # flags = ('n', 'nr', 'ns')
        # stopwords=pd.read_csv('cn_stopwords.txt')
        # print(type(stopwords))
        # for sentence in list1:
        #     word = [w.word for w in pseg.cut(sentence) if w.flag in flags and w.word not in stopwords]
        #     words.append(word)
        # dct = Dictionary(words)
        # lda = models.ldamodel.LdaModel(corpus=corpus_bow, id2word=dct, num_topics=2)
        # df = df.append(df2,ignore_index=True)
        # print(words)
    # df.to_csv('test.csv')
from urllib.request import urlopen
from bs4 import BeautifulSoup
from jieba.analyse import extract_tags
from pyecharts import WordCloud
def t4():
    mask = imageio.imread(r"ditu.png")  # 用于最后图像图形

    f = open('l.txt','r',encoding='utf-8')
    source = f.read()
    keywords_textrank = jieba.analyse.textrank(source, withWeight=True,topK=100)
    # df2 = pd.DataFrame()
    # df2['word'] = [list1]
    # ll.append(keywords_textrank)
    df2 = pd.DataFrame()
    print(keywords_textrank)
    first, snd = zip(*keywords_textrank)
    wordcloud = WordCloud(width=1300, height=620)
    wordcloud.add("", first, snd, word_size_range=[20, 100])
    wordcloud.render('关键词.html')

def main():
    # t1()
    # t2()
    t4()
main()