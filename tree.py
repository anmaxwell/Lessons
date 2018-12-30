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
        return "Node: children:{}, metadata: {}".format(len(self.children), self.metadata )
      
      
#anode = Node('firstNode', 1)
#print(anode)
#
#secondnode = Node('secondNode', 2)
#print(secondnode.name)
#
#thirdnode = Node('thirdNode', 3)


initinput = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'


#root = Node('root')
def printChildren(node, counter):
    for i in range(len(node.children)):
        currentNode = node.children[i]
        print("    "*counter, currentNode)
        counterNext = counter+1
        printChildren(currentNode,counterNext)

def readChild(initinput):

    inputlist = initinput.split()
    leninputlist = len(inputlist)
    nodename = 0
    
    while leninputlist >0:
    
        anode = Node(nodename)
        nodename+=1
        firstchar = int(inputlist[0])
        secchar = int(inputlist[1])
        print(firstchar, secchar, inputlist)
        inputlist.pop(0)
        inputlist.pop(0)

        
        if firstchar==0:
            for j in range(secchar):
                anode.addMeta(inputlist[0])
                inputlist.pop(0)
        else:        
            #read meta
            for j in range(secchar):
                anode.addMeta(inputlist[-1])
                inputlist.pop()
      
            #read children for this anode
            
            
            #anode.addChild(child)
            
        

    #print(inputlist)

#    nn = Node("aChil")
#    nn.addMeta(666)
#
#    ii = Node("anotherChil")
#    ii.addMeta(9)
#    ii.addMeta(99)
#    
#    yy = Node("ThirdLayer")
#    yy.addMeta(7)
#    ii.addChild(yy)
#
#    anode.addChild(nn)
#    anode.addChild(ii)
    
#    print(anode.children[0])
    print()
    print("Root:", anode)
    printChildren(anode, 1)        
    print()
    return anode
        

readChild(initinput)
        







