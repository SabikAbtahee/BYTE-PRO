class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None
        self.parent = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        newNode = Node(val)
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:

                        current.left = newNode
                        current.left.parent = current
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = newNode
                        current.right.parent = current
                        break
                else:
                    break

    def inOrder(self,node):
        if(node == None): return
        self.inOrder(node.left)
        print(node.info)
        self.inOrder(node.right)

    def getHeight(self,node):
        if(node == None): return -1
        l = self.getHeight(node.left)
        r = self.getHeight(node.right)

        return max(l,r)+1


    def getHightOfDistintNode(self,node,data):
        if (node == None): return -1



        l = self.getHeight(node.left)
        r = self.getHeight(node.right)

        return max(l, r) + 1








tree = BinarySearchTree()
t = int(input())




for _ in range(t):
    x = int(input())
    tree.create(x)

def height(node=tree.root):
    return tree.getHeight(node)

tree.printTopView(tree.root)
