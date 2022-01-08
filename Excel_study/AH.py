import re
import pandas as pd
import time
import os
#读取lua文件
readfile=open('./TradeSkillMaster.lua',"r",encoding="UTF-8")
#读取itemID
itemID=pd.read_excel('./itemID.xlsx',index_col=0)
itemIDs = pd.DataFrame(itemID)
#读取已存excel文件，如果没有就不管
paths=[]
path = os.listdir('./ServerData/')
for j in path:
    k = j.split('/')
    k=k[-1]
    k=k.split('.')
    k=k[0]
    paths.append(k)
    # print(paths)
#提取lua中关键信息
#按行读取lua文件
f1 = readfile.readlines()
#定义行
newline = []
#定义关键字符串
r = "itemString,minBuyout,marketValue,numAuctions,quantity,lastScan"
#遍历每一行
for line in f1:
    #如果关键字符串在这一行就把这一行添加到定义的行内，提取需要的AH数据
    if r in line:
        newline.append(line)
#定义一个空列表
m = []
#将提取的AH数据按照"分割开，分割后的数据放入空列表，将服务器信息和AH信息分割开
for i in newline:
    s=i.split('"')
    m.append(s)
# for aa in m:
#     sheet_name=[]
#     dataperserver=[]
#     for i in range(len(m)):
#         sn = m[i][1]
#         datan = m[i][3]
#         dataperserver.append(sn)
#         dataperserver.append(datan)
#         servername = dataperserver[0]
#         serverdata = dataperserver[1]
#         servername = servername.split('@')
#         servername = servername[1]
#         serverdatas = []
#         serverdata = serverdata.split('\\')
#         serverdatas.append(serverdata)

#         for j in serverdatas:
#         #遍历每一行的数据
#             for m in j:
# #             #将数据按照，分割开
#                 m=m.split(',')
#                 #分割后加入到aa列表中
#                 aa.append(m)
#                 #将分割后的数据转换成dataframe
#                 df = pd.DataFrame(aa,columns=aa[0])
#                 #清理掉dataframe中的字符
#                 df = df[~df['lastScan'].isin(['lastScan'])]
#                 #将dataframe中的后面几列转换为int格式
#                 df[['minBuyout','marketValue','numAuctions','quantity','lastScan']]=df[['minBuyout','marketValue','numAuctions','quantity','lastScan']].astype('int64')
#         print(df)
#                 #建立一个datetime的列表
#                 # datetime=[]



# #定义一个列表，用于存放服务器名字
# sheet_name=[]
# #定义一个空列表，用于存放AH数据
# data=[]
# #在AH信息中提取服务器名字和AH数据，分别放入sheetname和data
# for i in range(len(m)):
#     sn = m[i][1]
#     datan = m[i][3]
#     sheet_name.append(sn)
#     data.append(datan)

# #定义两个列表
# # datas=[]
# # aa=[]
# #在data里面遍历
# for i in data:
#     sheets=[]
#     for sheet in sheet_name:
#         sheet=sheet.split('@')
#         sheet=sheet[1]
#         sheets.append(sheet)
#     datas=[]
#     aa=[]
#     #将data里的数据分行
#     i = i.split('\\')
#     #分行后的数据添加到datas
#     datas.append(i)
#     #在分行后的数据里面遍历
#     for j in datas:
#         #遍历每一行的数据
#         for m in j:
#             #将数据按照，分割开
#             m=m.split(',')
#             #分割后加入到aa列表中
#             aa.append(m)
#             #将分割后的数据转换成dataframe
#             df = pd.DataFrame(aa,columns=aa[0])
#             #清理掉dataframe中的字符
#             df = df[~df['lastScan'].isin(['lastScan'])]
#             #将dataframe中的后面几列转换为int格式
#             df[['minBuyout','marketValue','numAuctions','quantity','lastScan']]=df[['minBuyout','marketValue','numAuctions','quantity','lastScan']].astype('int64')
#             #建立一个datetime的列表
#             datetime=[]
#             #在lastscan这一列遍历
#     for j in df['lastScan']:
#             #将每一个时间戳转化为时间格式
#         j=time.localtime(j)
#                 #格式化时间格式
#         j = time.strftime("%Y-%m-%d %H:%M",j)
#                 #将转化后的数据写入datetime
#         datetime.append(j)
#             #将转化后的数据添加到df里面，形成最终的df
#     df['datetime']=datetime
#             #将物品ID列的ni：去掉
#     df['itemString']=df['itemString'].map(lambda x: x.lstrip('ni:'))
#             #将物品ID转化为数字格式
#     df['itemString']=df['itemString'].astype('int64')
#     #将df和itemID进行对应形成新df
#     df = pd.merge(df,itemIDs,left_on='itemString',right_on='ID')
#         #在所有excel里面遍历
#     for sheet in sheets:
#         if os.path.isfile('./ServerData/{}.xlsx'.format(sheet)):
#             for jj in paths:
#                 if jj == sheet:
#                     serverdata = pd.read_excel('./ServerData/{}.xlsx'.format(sheet),header=0,index_col=0)
#                     serverdata = pd.DataFrame(serverdata)
#                     df = pd.concat([df,serverdata],axis=0)
#                     df = df.drop_duplicates()
#                     df.to_excel('./ServerData/{}.xlsx'.format(sheet))
#                 else:    
#                     continue
#         else:
#                 df.to_excel('./ServerData/{}.xlsx'.format(sheet))
#                 break
    
                
                
#         df=pd.DataFrame()
#         datas=[]
#         aa=[]'''