class Node:
    def __init__(self, val_pos, val):
        self.val_pos = val_pos
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.head = None

    def addElement(self, val):
        if(self.head == None):
            self.head = Node(1, val)
            return(1)
        else:
            a = self.head
            while(a != None):
                val_pos = a.val_pos
                if(a.val < val):
                    a = a.right
                    exp = "2*val_pos+1"
                else:
                    a = a.left
                    exp = "2*val_pos"
            x = eval(exp)
            a = Node(x, val)
            return(x)

    def deleteElement(self, val):
        a = self.head
        while(a != None):
            if(a.val < val):
                a = a.right
            elif(a.val > val):
                a = a.left
            else:
                x = a.val_pos
                a = None
        return(x)


Q = int(input())
BinarySearchTree = BST()
for i in range(Q):
    a = input().split(" ")
    if(a[0] == "i"):
        print(BinarySearchTree.addElement(int(a[1])))
    else:
        print(BinarySearchTree.deleteElement(int(a[1])))
