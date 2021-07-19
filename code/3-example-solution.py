from treelib import Node, Tree

tree = Tree()
tree.create_node("A", 25)
tree.create_node("B", 16, parent=25)
tree.create_node("C", 33, parent=25)
tree.create_node("D", 39, parent=33)
tree.create_node("E", 5, parent=16)
tree.create_node("F", 24, parent=16)
tree.create_node("G", 30, parent=33)
tree.show()

iot = [node for node in tree.nodes]
iot.sort()
print(iot) # [5, 16, 24, 25, 30, 33, 39]