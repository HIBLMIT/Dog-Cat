import openpyxl

wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='new title'
sheet['A1']='漫威宇宙'
rows=[['mei','1','2'],['1','2','3','4']]
for i in rows:
    sheet.append(i)
print(rows)
wb.save("C:/Users/imi2szh/PycharmProjects/test.xlsx")

print('ok')


