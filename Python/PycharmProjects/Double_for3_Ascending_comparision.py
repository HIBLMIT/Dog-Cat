list01 = [3,80,45,5,7,1]
list02 = [3,80,45,45,80,1]

"""
升序
"""
#取数据
for r in range(len(list01)-1):
    #作比较
     for c in range(r+1,len(list01)):
         if list01[r] > list01[c]:
             list01[r], list01[c] =list01[c],list01[r]

print(list01)

"""
降序
"""
#取数据
for r in range(len(list01)-1):
    #作比较
     for c in range(r+1,len(list01)):
         if list01[r] < list01[c]:
             list01[r], list01[c] =list01[c],list01[r]

print(list01)

"""
列表中有相同的数值
"""

#结果：假设没有相同项
result =False
for r in range(0,len(list02)-1):
    for c in range(r+1,len(list02)):
        if list02[r] == list02[c]:
            print("具有相同项")
            result = True
    #         break  # 退出内循环
    # if result:
    #     break # 退出外循环          #注释掉的三行是解决只要有相同项就退出循环，而不用打印多个相同项

if result == False:
    print("没有相同项")
