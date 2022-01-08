import os
import xlrd
import pandas as pd
filePath = 'D:/OneDrive/SynologyDrive/常用报表审批表格式/量收分析/清单月报'
f_name = os.listdir(filePath)
source_xls= []
for i in f_name:
    source_xls.append(filePath + '/' + i)
target_xls = r"D:/OneDrive/SynologyDrive/常用报表审批表格式/量收分析/py汇总表.xlsx"
print('正在读取数据')
data = []
for i in source_xls:
    wb = pd.read_excel(i)
    wb = pd.DataFrame(wb)
    m = i.split('/')
    n = m[-1:]
    date = n[0][:-4]
    date = date[:4]+'-'+date[5:-1]
    # print(month)
    wb['年月']=date
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