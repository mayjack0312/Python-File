# coding=utf-8
import os
import xlwt
import sys
 
file_path = sys.path[0]+'\\filenamelist.xls'
f = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = f.add_sheet('sheet1')
pathDir = os.listdir(sys.path[0])
 
i = 0
for s in pathDir:
    sheet.write(i, 0, s)
    i = i+1
            
print(file_path)
print(i)
f.save(file_path)
