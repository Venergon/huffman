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
    def __init__(self, nodes):
        self.nodes = nodes
        self.probability = sum([x.get_prob() for x in self.nodes])

    def __str__(self):
        return "({})".format(", ".join(map(str, self.nodes)))

    def get_prob(self):
        return self.probability

    def get_val(self):
        return sum([x.get_val() for x in self.nodes])

    def set_code(self, code):
        self.code = code

    def get_code(self):
        return self.code

def split_nodes(node):
    code = node.get_code()
    for i,n in enumerate(node.nodes):
        n.set_code(code+str(i))
        if type(n) is NodeJoin:
            split_nodes(n)
        else:
            final_codes.append(n)

nodes = []

radix = int(input("Enter Radix: "))
n = input("Enter node: ")
while n:
    value, probability = n.split(",")
    probability = float(probability)
    nodes.append(Node(value, probability))
    n = input("Enter node: ")

while len(nodes) % radix != 1:
    nodes.append(Node("dummy", 0))

if sorted(nodes, key=lambda x: x.get_prob(), reverse=True) != nodes:
    print("Nodes not sorted! Sorting...")
    nodes.sort(key=lambda x: x.get_prob(), reverse=True)
    print("New nodes:")
    for node in nodes:
        print("  "+str(node))

while len(nodes) > 1:
    new_nodes = nodes[:-radix]
    new_node = NodeJoin(nodes[-radix:])
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
    if str(node) != "(dummy)":
        print("Node {} has code {}".format(node, node.get_code()))


