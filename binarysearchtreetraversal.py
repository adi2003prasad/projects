# the data can be represented as
# {node:[child, child], child:[childofchild, childofchild], ...}

class node():
    def __str__(self) -> str:
        return str([self.node, self.right, self.left, self.parent])

    def __init__(self, left, right, node_data, parent) -> None:
        self.node = node_data
        self.left = left
        self.right = right
        self.parent = parent


class tree():
    def __init__(self, nodeDict) -> None:
        self.nodeDict = nodeDict

    def node_definer(self, node_lists, node_data):
        parent = None
        for x in self.nodeDict:
            print(x)
            if (node_data in self.nodeDict[x]):
                parent = x
            else:
                pass
        if parent:
            return node(node_lists[0], node_lists[1], node_data, parent)
        else:
            return node(node_lists[0], node_lists[1], node_data, None)

    def initializer(self):
        self.nodes = []
        for x in self.nodeDict:

            self.nodes.append(self.node_definer(
                self.nodeDict[x], x))

    def rec_left_goer(self, node_t):
        if(node_t.left == None):
            return node_t
        else:
            return self.rec_left_goer(node_t.left)

    def data_fetcher(self, x):
        # going down the map
        if(x.right != None):
            return self.rec_left_goer(x.right)
        # that is going up
        parent = x.parent
        child = x
        while(parent.right == child):
            if (parent.parent == None):
                return parent
            else:
                parent = parent.parent
                child = parent

    # done looking for things in the loop
data = {10: [9, 11], 9: [6, 12], 6: [2, 7], 12: [1, None]}
obj = tree(data)
obj.initializer()
print(obj.nodes[3].left)
# obj.data_fetcher(obj.nodes[3])
