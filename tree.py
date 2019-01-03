#%%

class Node:
    'Common base class for all nodes'

    def __init__(self, name):
        self.name = name
        self.metadata = []
        self.children = []
        
    def addMeta(self, value):
        self.metadata.append(value)
        
    def addChild(self,childNode):
        self.children.append(childNode)
      
    def __repr__(self):
        return "Node:{}, children:{}, metadata: {}".format(self.name, len(self.children), self.metadata )
      
      
#anode = Node('firstNode')
#print(anode)
#
#secondnode = Node('secondNode', 2)
#print(secondnode.name)
#
#thirdnode = Node('thirdNode', 3)

initinput0 = '0 1 99'
initinput1 = '1 1 0 1 99 2'
initinput2 = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'

def createTree(initinput):

    inputlist = initinput.split()
    
    i=0
    while i <len(initinput)-1:
        
        anode = Node(i)
        print(initinput[i])
     
        firstchar = int(inputlist[i])
        print(firstchar)
        secchar = int(inputlist[i+1])
        print(secchar)

        
        if firstchar==0:
            for j in range(secchar):
                anode.addMeta(inputlist[2])
            i+=1
            
        if i <len(initinput)-1:
            break

        else:        
            #read meta
            i+=1
            print("this node has children")
#            for j in range(secchar):
#                anode.addMeta(inputlist[-1])
#                inputlist.pop()
    