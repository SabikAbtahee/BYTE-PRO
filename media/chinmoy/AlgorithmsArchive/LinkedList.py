

<<<<<<<<<< Sabik

class Node():

    def __init__(self,data):
        self.data=data
        self.nextNode= None
        self.prevNode = None

    def getData(self):
        return self.data

    def setData(self,data):
        self.data=data

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self,nextNode):
        self.nextNode=nextNode

    def getPrevNode(self):
        return self.prevNode

    def setPrevNode(self,prevNode):
        self.prevNode=prevNode


class LinkedList:

    def __init__(self):
        self.root = None
        self.size = 0

    def addNodeInTail(self,data):
        tempNode = self.root
        tempNode2 = self.root
        if(tempNode == None):
            self.root = Node(data)
            self.root.setPrevNode(None)
            self.root.setNextNode(None)
        else:
            while(tempNode.getNextNode() != None):
                tempNode2 = tempNode
                tempNode = tempNode.getNextNode()
                tempNode.setPrevNode(tempNode2)

            tempNode.setNextNode(Node(data))
            tempNode.getNextNode().setPrevNode(tempNode)
            tempNode.getNextNode().setNextNode(None)

            # tempNode.setNextNode(None)
            # tempNode2.setNextNode(tempNode.getNextNode())

        self.size+=1


    def addNodeInTheHead(self,data):

        tempNode = self.root
        if(tempNode==None):
            self.root = Node(data)
            self.root.setPrevNode(None)
            self.root.setNextNode(None)
        else:
            newNode = Node(data)
            newNode.setNextNode(self.root)
            newNode.setPrevNode(None)
            self.root=newNode
            tempNode.setPrevNode(self.root)


        self.size+=1

    def InsertNth(self, head, data, position):
        index  = position
        newNode = Node(data)
        tempNode = self.root

        if(tempNode==None):
            self.root = newNode

        else:
            if(index == 0):

                newNode.setNextNode(self.root)
                self.root.setPrevNode(newNode)

                self.root = newNode
            else:
                count = 0
                flag = False
                while tempNode.getNextNode() != None:

                    if (count == index):

                        newNode.setNextNode(tempNode)
                        tempNode.getPrevNode().setNextNode(newNode)

                        tempNode.setPrevNode(newNode)
                        newNode.setPrevNode(tempNode.getPrevNode())

                        flag = True

                    tempNode = tempNode.getNextNode()
                    count += 1

                if (flag == False):

                    newNode.setNextNode(tempNode)
                    tempNode.getPrevNode().setNextNode(newNode)

                    tempNode.setPrevNode(newNode)
                    newNode.setPrevNode(tempNode.getPrevNode())

                    flag = True


                    newNode.setPrevNode(tempNode)
                    tempNode.setNextNode(newNode)

                if (flag == False):

                    newNode.setPrevNode(tempNode)
                    tempNode.setNextNode(newNode)

        self.size += 1

    def insertNodeAtIndex(self, index,data):
        if(index>=0 and index<self.size):
            tempNode = self.root

            flag = False
            count = 0

            newNode = Node(data)

            if (index == 0):

                newNode.setNextNode(self.root)
                self.root.setPrevNode(newNode)

                self.root = newNode

            else:
                # it will execute index 1 to size-1 . but index 1 will not be counted
                while tempNode.getNextNode() != None:
                    # print(count,index)
                    if (count == index):
                        # print(tempNode.)
                        newNode.setNextNode(tempNode)
                        tempNode.getPrevNode().setNextNode(newNode)

                        tempNode.setPrevNode(newNode)
                        newNode.setPrevNode(tempNode.getPrevNode())

                        flag = True

                    tempNode = tempNode.getNextNode()
                    count += 1

                if (flag == False):
                    print(tempNode.getData())
                    newNode.setPrevNode(tempNode)
                    tempNode.setNextNode(newNode)

            self.size += 1


        elif(index >= self.size): print("Index must be in 0 -", self.size-1, "range.")
        else: print("Index must be in positive")




    def insertNodeSorted(self, data):

        tempNode = self.root

        flag = False
        count = 0

        newNode = Node(data)

        if(tempNode==None):
            self.root = newNode
            self.size += 1
        else:
            if (newNode.getData() < tempNode.getData()):

                newNode.setNextNode(self.root)
                self.root.setPrevNode(newNode)

                self.root = newNode

            else:
                # it will execute index 1 to size-1 . but index 1 will not be counted
                while tempNode.getNextNode() != None:
                    # print(count,index)
                    if (data < tempNode.getData()):
                        # print(tempNode.)
                        newNode.setNextNode(tempNode)
                        tempNode.getPrevNode().setNextNode(newNode)

                        tempNode.setPrevNode(newNode)
                        newNode.setPrevNode(tempNode.getPrevNode())

                        flag = True

                    tempNode = tempNode.getNextNode()
                    count += 1

                if (flag == False):
                    print(tempNode.getData())
                    newNode.setPrevNode(tempNode)
                    tempNode.setNextNode(newNode)

        self.size += 1




    def getSize(self):
        return self.size


    def showList(self):
        tempNode = self.root
        print("[",end=' ')
        while(tempNode.getNextNode()!=None):
            print(tempNode.getData(),end=', ')
            tempNode = tempNode.getNextNode()
        print(tempNode.getData(),end='')
        print(" ]")


    def printList(self):
        tempNode = self.root

        while (tempNode.getNextNode() != None):
            print(tempNode.getData(),end=' ')
            tempNode = tempNode.getNextNode()
        print(tempNode.getData())



    def getHead(self): #return data only
        return self.root



ll = LinkedList()



n = int(input())
for i in range(n):
    n, m = input().strip().split(' ')
    ll.InsertNth(None,int(n),int(m))
    ll.printList()
    # print('executed',int(n),int(m))
#################################
print('loop end')


# ll.showListReversely()

                 if (count == index):

                        newNode.setNextNode(tempNode)
                        tempNode.getPrevNode().setNextNode(newNode)

                        tempNode.setPrevNode(newNode)
                        newNode.setPrevNode(tempNode.getPrevNode())

                        flag = True

                    tempNode = tempNode.getNextNode()
                    count += 1

                if (flag == False):

                    newNode.setNextNode(tempNode)
                    tempNode.getPrevNode().setNextNode(newNode)

                    tempNode.setPrevNode(newNode)
                    newNode.setPrevNode(tempNode.getPrevNode())

                    flag = True


                    newNode.setPrevNode(tempNode)
                    tempNode.setNextNode(newNode)

                if (flag == False):

                    newNode.setPrevNode(tempNode)
                    tempNode.setNextNode(newNode)

        self.size += 1

    def insertNodeAtIndex(self, index,data):
        if(index>=0 and index<self.size):
            tempNode = self.root

            flag = False
            count = 0

            newNode = Node(data)

            if (index == 0):

                newNode.setNextNode(self.root)
                self.root.setPrevNode(newNode)

                self.root = newNode

            else:
                # it will execute index 1 to size-1 . but index 1 will not be counted
                while tempNode.getNextNode() != None:
                    # print(count,index)
                    if (count == index):
                        # print(tempNode.)
                        newNode.setNextNode(tempNode)
                        tempNode.getPrevNode().setNextNode(newNode)

                        tempNode.setPrevNode(newNode)
                        newNode.setPrevNode(tempNode.getPrevNode())

                        flag = True

                    tempNode = tempNode.getNextNode()
                    count += 1

                if (flag == False):
                    print(tempNode.getData())
                    newNode.setPrevNode(tempNode)
                    tempNode.setNextNode(newNode)

            self.size += 1


        elif(index >= self.size): print("Index must be in 0 -", self.size-1, "range.")
        else: print("Index must be in positive")




    def insertNodeSorted(self, data):

        tempNode = self.root

        flag = False
        count = 0

        newNode = Node(data)

        if(tempNode==None):
            self.root = newNode
            self.size += 1
        else:
            if (newNode.getData() < tempNode.getData()):

                newNode.setNextNode(self.root)
                self.root.setPrevNode(newNode)

                self.root = newNode

            else:
                # it will execute index 1 to size-1 . but index 1 will not be counted
                while tempNode.getNextNode() != None:
                    # print(count,index)
                    if (data < tempNode.getData()):
                        # print(tempNode.)
                        newNode.setNextNode(tempNode)
                        tempNode.getPrevNode().setNextNode(newNode)

                        tempNode.setPrevNode(newNode)
                        newNode.setPrevNode(tempNode.getPrevNode())

                        flag = True

                    tempNode = tempNode.getNextNode()
                    count += 1

                if (flag == False):
                    print(tempNode.getData())
                    newNode.setPrevNode(tempNode)
                    tempNode.setNextNode(newNode)

        self.size += 1




    def getSize(self):
        return self.size


    def showList(self):
        tempNode = self.root
        print("[",end=' ')
        while(tempNode.getNextNode()!=None):
            print(tempNode.getData(),end=', ')
            tempNode = tempNode.getNextNode()
        print(tempNode.getData(),end='')
        print(" ]")


    def printList(self):
        tempNode = self.root

        while (tempNode.getNextNode() != None):
            print(tempNode.getData(),end=' ')
            tempNode = tempNode.getNextNode()
        print(tempNode.getData())



    def getHead(self): #return data only
        return self.root



ll = LinkedList()



n = int(input())
for i in range(n):
    n, m = input().strip().split(' ')
    ll.InsertNth(None,int(n),int(m))
    ll.printList()
    # print('executed',int(n),int(m))
#################################
print('loop end')


# ll.showListReversely()

>>>>>>>>>>
