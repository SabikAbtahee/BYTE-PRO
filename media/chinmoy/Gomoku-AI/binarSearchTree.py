from random import randrange, uniform

class Node():
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.leftChild = None
        self.rightChild = None
        self.height = -1;

    def setLeftChild(self,leftChild):
        self.leftChild=leftChild

    def setRightChild(self,rightChild):
        self.rightChild=rightChild

    def setParent(self,parent):
        self.parent=parent

    def setData(self,data): # update data
        self.data=data

    def setHeight(self,height):
        self.height=height

    def getData(self):
        return self.data

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def getParent(self):
        return self.parent




class BinarySearchTree():

    def __init__(self):
        self.root = None
        self.size = 0

    def getRoot(self):
        return self.root

    def insertNode(self, data):
        tempNode = self.root

        newNode = Node(data)
        if(tempNode == None):
            self.root = newNode

        else:
            while(True):
                if(data < tempNode.getData()):
                    if(tempNode.getLeftChild() == None):
                        tempNode.setLeftChild(newNode)
                        tempNode.getLeftChild().setParent(tempNode)
                        break
                    else:
                        tempNode = tempNode.getLeftChild()
                else:
                    if (tempNode.getRightChild() == None):
                        tempNode.setRightChild(newNode)
                        tempNode.getRightChild().setParent(tempNode)

                        break
                    else:
                        tempNode = tempNode.getRightChild()
        self.size+=1

    def findNode(self,data):
        tempNode = self.root
        iteration =0
        while(True):
            if(tempNode.getData()==data):

                return iteration
            elif(tempNode.getData()>data): tempNode=tempNode.getLeftChild()
            else: tempNode=tempNode.getRightChild()
            iteration+=1

    def printTreeInOrder(self, node):
        if(node == None): return
        self.printTreeInOrder(node.getLeftChild())
        print(node.getData(),end=' ')
        self.printTreeInOrder(node.getRightChild())


    def printTreePostOrder(self, node):
        if(node == None): return
        self.printTreeInOrder(node.getRightChild())
        print(node.getData(),end=' ')
        self.printTreeInOrder(node.getLeftChild())


    def printTreePreOrder(self, node):
        if(node == None): return
        print(node.getData(),end=' ')
        self.printTreePreOrder(node.getLeftChild())
        self.printTreePreOrder(node.getRightChild())

    def deleteNode(self,data):
        tempNode = self.findNode(data)
        # print(tempNode.getData())
        # print(tempNode.getParent().getData())
        # if(tempNode.getLeftChild()): print(tempNode.getLeftChild().getData())
        # if(tempNode.getRightChild()): print(tempNode.getRightChild().getData())
        if(tempNode.getLeftChild()==None and tempNode.getRightChild()==None):
            if(tempNode.getParent().getData()>tempNode.getData()):
                tempNode.getParent().setLeftChild(None)
            else:
                tempNode.getParent().setRightChild(None)

        elif(tempNode.getLeftChild() == None and tempNode.getRightChild() != None):
            child = tempNode.getRightChild()
            parent = tempNode.getParent()

            parent.setRightChild(child)

        elif (tempNode.getLeftChild() != None and tempNode.getRightChild() == None):
            child = tempNode.getLeftChild()
            parent = tempNode.getParent()

            parent.setLeftChild(child)
        else:
            child = tempNode.getRightChild()

            while(child.getLeftChild()!=None):
                child = child.getLeftChild()
            tempNode.setData(child.getData())
            child.getParent().setLeftChild(None)
            # tempNode.setData(child.getData())

        self.size-=1

    def getHeight(self,node):

        if(node == None): return -1

        # if(node and node.getLeftChild()): print('Calling node= ', node.getData(),"left Child= ",node.getLeftChild().getData())
        leftHeight = self.getHeight(node.getLeftChild())

        # if(node and node.getRightChild()): print('Calling node = ', node.getData(),"right Child= ",node.getRightChild().getData())
        RightHeight = self.getHeight(node.getRightChild())


        # print(maxH)
        return max(leftHeight,RightHeight)+1





binary = BinarySearchTree()

binary.insertNode(12)
binary.insertNode(20)
binary.insertNode(6)
binary.insertNode(4)
binary.insertNode(5)
binary.insertNode(25)
binary.insertNode(21)
binary.insertNode(29)
binary.insertNode(19)
binary.insertNode(27)
binary.insertNode(26)
binary.insertNode(28)





# list = input().strip().split(' ')
# l = input()
# arr = input()
# list=list(map(int,arr.split(' ')))
# for i in range(len(list)):
#     binary.insertNode(list[i])
binary.printTreeInOrder(binary.getRoot())
print()
print(binary.findNode(4))
# binary.printTreePostOrder(binary.getRoot())
# binary.printTreePreOrder(binary.getRoot())