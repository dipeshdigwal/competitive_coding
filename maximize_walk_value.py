class node:
    def __init__(self,v,id):
        self.id=id
        self.val=v
        self.right=None
        self.left=None

class bin_tree:
    def __init__(self):
        self.head=None

    def addNode(self,v,parent):
        if(self.head==None):
            self.head=node(v,1)
        else:
            a=self.head
            while(a.right!=None):
                a=a.right

a=input().split(" ")
[N,NSP,Q]=[int(i) for i in a]
V=input().split(" ")
C=input().split(" ")
SN=input().split(" ")
for i in range(Q):
    b=input().split(" ")
    [SNODE,DNODE,W]=[int(i) for i in b]