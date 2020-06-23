class Node:
    def __init__(self, val, val_pos):
        self.val_pos=val_pos
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def addElement(self, x, b):
        if(self.root == None):
            self.root = Node(x,1)
            return(1)
        else:
            if(x <= b.val):
                if(b.left == None):
                    b.left = Node(x)
                else:
                    self.addElement(x, b.left)
            else:
                if(b.right == None):
                    b.right = Node(x)
                else:
                    self.addElement(x, b.right)


Q = int(input())
BinarySearchTree = BST()
for i in range(Q):
    a = input().split(" ")
    if(a[0] == "i"):
        print(BinarySearchTree.addElement(int(a[1]), BinarySearchTree.root))
    # else:
    #    print(BinarySearchTree.deleteElement(int(a[1])))
