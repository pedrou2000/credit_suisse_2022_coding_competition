from typing import List

# The Node class will contain the information of the nodes of a tree
# represented by a dictionary containing all the nodes. By representing
# the transactions as a tree is easy to find out if there was an 
# ineligeble transaction 

class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = set()
        self.ancestors = set()

    def add_child(self, child):
        # transactions between the same user do not affect
        if child is not self:
            self.children.add(child)
            child.add_ancestor(self)

    def add_ancestor(self, ancestor):
        self.ancestors.add(ancestor)
    
    def add_ancestors(self, ancestors):
        self.ancestors.update(ancestors)

    def __str__(self) -> str:
        return str(self.data)
    
    # for depuration purporses
    def print_node(self) -> str:
        buffer = 'Node: '
        buffer += str(self.data)
        buffer += '\n'
        buffer += 'Ancestors: '
        for ancestor in self.ancestors:
            buffer += str(ancestor)
        buffer += '\n'
        buffer += 'Children: '
        for child in self.children:
            buffer += str(child)
        buffer += '\n'
        buffer += '\n'
        print(buffer)

def solution(n: int, l: int, transfers: List[List[int]]) -> bool:
    # I create the nodes dicitionary which contains the nodes that appear on the 
    # transactions. The dictionary nodes will represent the tree structure.
    nodes = dict() 
    for sender, receiver in transfers:
        if sender not in nodes.keys():
            nodes[sender] = Node(sender)
        if receiver not in nodes.keys():
            nodes[receiver] = Node(receiver)

    # for each of the transfers the receiver is added as child of the sender
    for transfer in transfers:        
        nodes[transfer[0]].add_child(nodes[transfer[1]])

    # I complete the ancestors fields of each node
    for node in nodes.values():
        for child in node.children:
            child.add_ancestors(node.ancestors)

    # check there are no loops in the tree, if there are it is because 
    # there was an ineligible transaction
    for node in nodes.values():
        if node in node.ancestors:
            return True

    return False


"""
def main():
    n, l = [int(i) for i in input().split(" ")]
    transfers = []
    for i in range(l):
      line = input().split(" ")
      transfers.append([int(line[0]), int(line[1])])

    result = solution(n, l, transfers)
    print("Ineligible" if result else "Eligible")
    
if __name__ == '__main__':
    main()
"""
print(solution(4, 5, [
    [0, 1],
    [1, 2],
    [1, 3],
    [2, 0],
    [3, 2],
]))
print(solution(3, 2, [
    [0, 1],
    [1, 1],
]))
