import pandas as pd
import time
import os

from pandas.core.frame import DataFrame
from funcs import key_in_lines_in_file

path = './TradeSkillMaster.lua'
readfile = open(path,"r",encoding="UTF-8")
f1 = readfile.readlines()
key = "type,amount,otherPlayer,player,time"
lines = key_in_lines_in_file(key,f1)
a = []
b=[]
for i in lines:
    a.append(i)
for i in a:
    i = i.split("=")
    b.append(i[1].split('\\'))
for i in b:
    