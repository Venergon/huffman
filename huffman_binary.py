#!/usr/local/bin/python3
final_codes = []
class Node:
    def __init__(self, value, probability):
        self.val = value
        self.probability = probability

    def __str__(self):
        return "({})".format(self.val)

    def get_prob(self):
        return self.probability

    def get_val(self):
        return self.val

    def set_code(self, code):
        self.code = code

    def get_code(self):
        return self.code

class NodeJoin:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        self.probability = node1.get_prob() + node2.get_prob()

    def __str__(self):
        return "({},{})".format(self.node1, self.node2)

    def get_prob(self):
        return self.probability

    def get_val(self):
        return self.node1.get_val()+self.node2.get_val()

    def set_code(self, code):
        self.code = code

    def get_code(self):
        return self.code

def split_nodes(node):
    code = node.get_code()
    node1, node2 = node.node1, node.node2
    node1.set_code(code+"1")
    node2.set_code(code+"0")

    if (type(node1) is NodeJoin):
        split_nodes(node1)
    else:
        final_codes.append(node1)

    if (type(node2) is NodeJoin):
        split_nodes(node2)
    else:
        final_codes.append(node2)

nodes = []

n = input("Enter node: ")
if "," not in n:
    print("No first node, maybe you were trying to set a radix? (This version only works with radix two)")
    n = input("Enter node: ")

while n:
    value, probability = n.split(",")
    probability = float(probability)
    nodes.append(Node(value, probability))
    n = input("Enter node: ")

if sorted(nodes, key=lambda x: x.get_prob(), reverse=True) != nodes:
    print("Nodes not sorted! Sorting...")
    nodes.sort(key=lambda x: x.get_prob(), reverse=True)
    print("New nodes:")
    for node in nodes:
        print("  "+str(node))

while len(nodes) > 1:
    new_nodes = nodes[:-2]
    new_node = NodeJoin(nodes[-1], nodes[-2])
    for i,obj in enumerate(new_nodes):
        if (new_node.get_prob() >= obj.get_prob()):
            new_nodes.insert(i, new_node)
            break
    else:
        new_nodes.append(new_node)
    nodes = new_nodes

assert(len(nodes) == 1)
node = nodes[0]
node.set_code("")
if type(node) is Node:
    final_codes.append(node)
else:
    split_nodes(node)

final_codes.sort(key = lambda x: x.get_val())
print()
for node in final_codes:
    print("Node {} has code {}".format(node, node.get_code()))


