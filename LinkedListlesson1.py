#%%
        
class DoublyNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        
    def fwdtraverse(self):
        node = self # start from the named node
        for i in range(6):
            print(node.val) # access the node value
            node = node.next # move on to the next node
            
    def bcktraverse(self):
        node = self # start from the named node
        for i in range(6):
            print(node.val) # access the node value
            node = node.prev # move on to the prev node
        
node1 = DoublyNode(12) 
node2 = DoublyNode(99) 
node3 = DoublyNode(37) 
node1.next = node2 # 12->99
node2.next = node3 # 99->37
node3.next = node1
node1.prev = node3
node3.prev = node2
node2.prev = node1
# the entire linked list now looks like: 12->99->37

node1.fwdtraverse()
print('\n')
node1.bcktraverse()