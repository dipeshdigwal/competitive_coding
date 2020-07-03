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

    def minValueNode(self, b):
        while(b.left is not None):
            b = b.left
        return(b)

    def delete(self, root, val, flag):
        if(val < root.val):
            root = self.delete(root.left, val, 1)
        elif(val > root.val):
            root = self.delete(root.right, val, 1)
        else:
            if(flag == 1):
                print(root.val_pos)
            if(root.left is None and root.right is None):
                root = None
            elif root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left
            else:
                x = self.minValueNode(root)
                x.val = x.val
                root = self.delete(root, x.val, 0)
        return(root)

    def deleteElement2(self, val, b):
        if(val < b.val):
            val_pos = self.deleteElement2(val, b.left)
        elif(val > b.val):
            val_pos = self.deleteElement2(val, b.right)
        else:
            if(b.left is None and b.right is None):
                val_pos = b.val_pos
                b = None
            elif(b.left is None):
                b = b.right
                val_pos = b.val_pos
            elif(b.right is None):
                b = b.left
                val_pos = b.val_pos
            else:
                x = self.minValueNode(b.right)
                b.val = x.val
                val_pos = b.val_pos
                self.deleteElement2(x.val, b.right)
        return(val_pos)


Q = int(input())
BinarySearchTree = BST()
for i in range(Q):
    a = input().split(" ")
    if(a[0] == "i"):
        print(BinarySearchTree.addElement(float(a[1]), BinarySearchTree.root))
    else:
        # print(BinarySearchTree.deleteElement2(
        #    float(a[1]), BinarySearchTree.root))
        BinarySearchTree.root = BinarySearchTree.delete(
            BinarySearchTree.root, int(a[1]), 1)
