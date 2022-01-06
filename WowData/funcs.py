import os
import pandas as pd
def file_name (dirname):
    #定义路径列表
    paths=[]
    #路径名称
    path = os.listdir(dirname)

    #在路径中遍历
    for j in path:
        k = j.split('/')
        k=k[-1]
        k=k.split('.')
        k=k[0]
        paths.append(k)
    return(paths)
def key_in_lines_in_file(key,file):
    newline = []
    #定义关键字符串
    r = key
    #遍历每一行
    for line in file:
        #如果关键字符串在这一行就把这一行添加到定义的行内，提取需要的AH数据
        if r in line:
            newline.append(line)
    return(newline)
def time_change(numoftime):
    j=time.localtime(numoftime)
    j = time.strftime("%Y-%m-%d %H:%M",j)
    return(j)
def serverdata(m):#在AH信息中提取服务器名字和AH数据，分别放入sheetname和data
    for j in range(len(m)):
        sheet_name=[]
        data=[]
        sn = m[j][1]
        datan = m[j][3]
        sheet_name = sheet_name.append(sn)
        data = data.append(datan)
    return(data)
