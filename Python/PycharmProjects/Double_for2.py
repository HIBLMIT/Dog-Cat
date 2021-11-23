"""
          外层4        内层
*                      0
**                     01
***                    012
****                   0123
"""

for r in range(4):           #range(start,stop,step)  计数从start开始，默认是从0开始；stop结束，但是不包括stop.
    for c in range(r+1):
        print("*",end = "")
    print()


#单行注释

'''
多行注释方法一
'''

"""
多行注释方法二
"""

# 注掉代码的快捷方式：ctrl+/

