# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 10:13:57 2020

@author: weisssun
"""


import os
import xlrd
import xlsxwriter
import pandas as pd


filePath = 'D:/OneDrive/SynologyDrive/常用报表审批表格式/量收分析/清单月报'
#需合并的文件所在的文件夹路径

f_name = os.listdir(filePath)
#读取文件夹内所有文件名
#print(f_name)

source_xls= []
for i in f_name:
    source_xls.append(filePath + '/' + i)
#将文件路径存储在列表中
#print(source_xls)

target_xls = r"D:/OneDrive/SynologyDrive/常用报表审批表格式/量收分析/汇总表.xlsx"
#合并后文件的路径
print('正在读取数据')
# 读取数据
data = []
for i in source_xls:
    wb = pd.read_excel(i)
    wb = pd.DataFrame(wb)
    m = i.split('/')
    n = m[-1:]
    date = n[0][:-4]
    date = date.split('年')
    year = date[0]+"年"
    month = date[1]
    print('.')
    # print(month)
    wb['年']=year
    wb['月']=month
    data.append(wb)
print('正在合并数据')
all_data = pd.concat(data)
ad = all_data.copy()
ad= pd.DataFrame(ad)
print("正在筛选机关军警行业数据")
bd = ad[ad['行业分类'].isin(["机关军警","政务机关"])]
# print(bd.head())
bd.to_excel(target_xls)
print('完成')
