from anytree import Node, RenderTree
from antlr4.tree.Tree import TerminalNodeImpl

def build_tree(antlr_node, parent=None):
    if isinstance(antlr_node, TerminalNodeImpl):
        label = antlr_node.getText()
    else:
        label = type(antlr_node).__name__.replace("Context", "")

    current = Node(label, parent=parent)

    for i in range(antlr_node.getChildCount()):
        build_tree(antlr_node.getChild(i), current)

    return current

def print_tree(antlr_tree):
    root = build_tree(antlr_tree)
    for pre, _, node in RenderTree(root):
        print(f"{pre}{node.name}")
