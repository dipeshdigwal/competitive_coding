class Node:
    def __init__(self, val, val_pos):
        self.val = val
        self.val_pos = val_pos
        self.left = None
        self.right = None


def insert(root, val, val_pos):
    if(root == None):
        root = Node(val, val_pos)
        print(val_pos)
    else:
        if(val <= root.val):
            root.left = insert(root.left, val, 2*val_pos)
        else:
            root.right = insert(root.right, val, 2*val_pos+1)
    return(root)


def minFinder(root):
    b = root
    while(b.left is not None):
        b = b.left
    return(b)


def delete(root, val, flag):
    if(root is None):
        return None
    elif(val < root.val):
        root.left = delete(root.left, val, flag)
    elif(val > root.val):
        root.right = delete(root.right, val, flag)
    else:
        if(flag == 1):
            print(root.val_pos)

        if(root.left is None and root.right is None):
            root = None
        elif (root.left is None):
            root = root.right
        elif(root.right is None):
            root = root.left
        else:
            x = minFinder(root.right)
            root.val = x.val
            root.right = delete(root.right, x.val, 0)
    return(root)


root = None
Q = int(input())
for i in range(Q):
    a = input().split(" ")
    if(a[0] == "i"):
        root = insert(root, int(a[1]), 1)
    else:
        root = delete(root, int(a[1]), 1)
