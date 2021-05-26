# 定义圣诞树函数，需要一个layers变量定义层数
def tree(layers):
    # range用于生成一个数组，从0到layers
    for leaf in range(layers):
        content = ' '*(layers-leaf) + '*'*(leaf*2+1)
        print(content)
    trunk = ' '*layers + '|'
    print(trunk)
    # 可以没有返回值
# 调用函数
tree(5)
# tree(12)
# # 在循环中调用
# for i in range(12):
#     layer = i+3
#     tree(layer)