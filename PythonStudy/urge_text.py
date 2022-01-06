import time

import urge

t1 = time.time()
city = ['乌鲁木齐', '广州']
lang = 'zh'
temp = []
for i in city:
    result = urge.get_simple_temp(i).once()
    print("{}的温度是{}°".format(i, result))
    temp.append(result)
温差 = temp[0] - temp[1]
if 温差 >= 0:
    print('{}与{}的温差是{}°'.format(city[0], city[1], 温差))
else:
    温差 = abs(温差)
    print('{}与{}的温差是{}°'.format(city[0], city[1], 温差))
t2 = time.time()
t1 = t2 - t1
print("程序运行时间{}秒".format(t1))
