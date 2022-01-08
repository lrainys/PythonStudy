import PySimpleGUI as sg
import pandas as pd
import time
import os
from funcs import key_in_lines_in_file
path = sg.popup_get_file('请选择有效的Tradeskillmaster.lua文件')
readfile=open('{}'.format(path),"r",encoding="UTF-8")
f1 = readfile.readlines()
itemID=pd.read_excel('./itemID.xlsx',index_col=0)
itemIDs = pd.DataFrame(itemID)
finaldata = pd.DataFrame()
key = 'itemString,minBuyout,marketValue,numAuctions,quantity,lastScan'
lines = key_in_lines_in_file(key,f1)
for a in lines:
    servers = []
    auctiondata = []
    data = []
    datetime = []
    server_and_auction_data = a.split('"')
    servername=server_and_auction_data[1]
    b = servername.split('@')
        #服务器名
    server = b[1]
    serverdata = server_and_auction_data[3]
    datas= serverdata.split('\\')
    for c in datas:
        auctiondata.append(c)
    for d in auctiondata:
        e = d.split(',')
        data.append(e)
    auctiondataframe = pd.DataFrame(data,columns=data[0])
    auctiondataframe = auctiondataframe[~auctiondataframe['lastScan'].isin(['lastScan'])]
    #将dataframe中的后面几列转换为int格式
    auctiondataframe[['minBuyout','marketValue','numAuctions','quantity','lastScan']]=auctiondataframe[['minBuyout','marketValue','numAuctions','quantity','lastScan']].astype('int64')
    for j in auctiondataframe['lastScan']:
    #将每一个时间戳转化为时间格式
        j=time.localtime(j)
        #格式化时间格式
        j = time.strftime("%Y-%m-%d %H:%M",j)
        #将转化后的数据写入datetime
        datetime.append(j)
auctiondataframe['lastScana']=datetime
auctiondataframe['itemString']=auctiondataframe['itemString'].map(lambda x: x.lstrip('ni:'))
                #将物品ID转化为数字格式
auctiondataframe['itemString']=auctiondataframe['itemString'].astype('int64')
        #将df和itemID进行对应形成新df
auctiondataframe = pd.merge(auctiondataframe,itemIDs,left_on='itemString',right_on='ID')
savepath = sg.popup_get_folder('请选择数据保存的文件夹')
if os.path.isfile('{}/{}.xlsx'.format(savepath,server)):
    serverdata = pd.read_excel(('{}/{}.xlsx'.format(savepath,server)), header=0, index_col=0)
    serverdata = pd.DataFrame(serverdata)
    auctiondataframe = pd.concat([auctiondataframe, serverdata], axis=0)
    auctiondataframe = auctiondataframe.drop_duplicates()
    auctiondataframe.to_excel('{}/{}.xlsx'.format(savepath,server))
else:
    auctiondataframe.to_excel('{}/{}.xlsx'.format(savepath,server))