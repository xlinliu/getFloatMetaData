# coding:utf-8
import xlrd
path=r'F:\杂项\党员工作\硕士1班花名册.xlsx'.decode('utf-8')
data=xlrd.open_workbook(path)
table=data.sheet_by_index(0)
nrows=table.nrows
print table.row_types(2)
