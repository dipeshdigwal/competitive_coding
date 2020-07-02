class Node:
    def __init__(self, val, val_pos):
        self.val_pos = val_pos
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def addElement(self, x, b):
        if(self.root == None):
            self.root = Node(x, 1)
            return(1)
        else:
            if(x <= b.val):
                if(b.left == None):
                    val_pos = 2*b.val_pos
                    b.left = Node(x, val_pos)
                else:
                    val_pos = self.addElement(x, b.left)
            else:
                if(b.right == None):
                    val_pos = 2*b.val_pos+1
                    b.right = Node(x, val_pos)
                else:
                    val_pos = self.addElement(x, b.right)
            return(val_pos)

    def deleteElement(self, val, b):
        if(self.root.val == val):
            val_pos = self.root.val_pos
            self.root = None
            return(val_pos)
        else:
            if(val <= b.val):
                if(b.left.val == val):
                    val_pos = b.left.val_pos
                    b.left = None
                else:
                    val_pos = self.deleteElement(val, b.left)
            else:
                if(b.right.val == val):
                    val_pos = b.right.val_pos
                    b.right = None
                else:
                    val_pos = self.deleteElement(val, b.right)
            return(val_pos)


Q = int(input())
BinarySearchTree = BST()
for i in range(Q):
    a = input().split(" ")
    if(a[0] == "i"):
        print(BinarySearchTree.addElement(int(a[1]), BinarySearchTree.root))
    else:
        print(BinarySearchTree.deleteElement(int(a[1]), BinarySearchTree.root))
