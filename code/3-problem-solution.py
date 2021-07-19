from treelib import Node, Tree

def create_tree(L):
    tree = Tree()
    tree.create_node(L[0], L[0])
    tree.create_node(L[1], L[1], parent=L[0])
    tree.create_node(L[2], L[2], parent=L[0])
    tree.create_node(L[3], L[3], parent=L[1])
    tree.create_node(L[4], L[4], parent=L[1])
    tree.create_node(L[5], L[5], parent=L[2])
    tree.create_node(L[6], L[6], parent=L[2])
    return tree

def find_closest(tree, target):
    nodes = [node for node in tree.nodes]
    return nodes[min(range(len(nodes)), key=lambda i: abs(nodes[i]-target))]

def remove_node(tree, value):
    tree.remove_node(value)
    return tree

L = list(map(int, input("List of 7 elements: ").split()))
tree = create_tree(L)
tree.show()

target = int(input("Target: "))
closest = find_closest(tree, target)
print(f"The closest node to the target of {target} is {closest}.")

value = int(input("Node to remove: "))
remove_node(tree, value)
tree.show()
print(f"Node {value} was removed.")