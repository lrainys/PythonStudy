#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LiuRui
# @data 
# @file main.py
from pygopus import WorkBook

workbook = WorkBook('./new.xlsx')
for i in workbook.sheets():
    print(i)
    sheet = workbook.get_sheet(i)
    print(sheet)

