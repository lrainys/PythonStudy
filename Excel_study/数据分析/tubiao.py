import numpy as np
import pandas as pd
 
import matplotlib.pyplot as plt
import matplotlib

df = pd.read_excel('D:/OneDrive/SynologyDrive/常用报表审批表格式/量收分析/py汇总表.xlsx',index_col=0)
df['年月']=pd.to_datetime(df['年月'],format='%Y-%m')
fig  = plt.figure()
ax2=fig.add_subplot(2,2,1)
sr = df.pivot_table(columns= '年月',index = '地市',values = ['全业务收入当月收入现金C网'])
sr=sr.dropna()
print(sr)
# sr.plot()
# plt.show()