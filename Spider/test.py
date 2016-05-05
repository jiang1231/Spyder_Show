#conding:utf-8
import xlrd

data = xlrd.open_workbook('result.xlsx')

table = data.sheets()[0]
print table
row = 1
 
col = 1
 
#  0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
ctype = 1 
value = u'string'
 
xf = 0
 
table.put_cell(row, col, ctype, value, xf)
 
table.cell(0,0)
 
table.cell(0,0).value