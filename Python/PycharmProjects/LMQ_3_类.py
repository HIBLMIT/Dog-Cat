class Tree():
    def __init__(self,leaf,layers):
        self.leaf=leaf
        self.layers=layers
    def ContentTrunk(self,leaf,layers):
        for leaf in range(layers):
            content = ' ' * (layers - leaf) + '*' * (leaf * 2 + 1)
            print(content)
            trunk = ' ' * layers + '|'
            print(trunk)

tree=Tree.ContentTrunk(9,5)
print(tree)
