class linkList:
    def __init__(self,v):
        self.val=v
        self.next=None

class adjList:
    def __init__(self,n):
        self.l=[linkList(i) for i in range(1,n+1)]
    def addEle(self,i,j):
        x=self.l[i-1]
        if(x!=None):
            while(x.next!=None):
                x=x.next
            x.next=linkList(j)
    def addVertex(self,a):
        x=a.split(" ")
        i=int(x[0])
        j=int(x[1])
        self.addEle(i,j)   #back linking not happening....
        self.addEle(j,i)
    def see(self):
        for i in range(len(self.l)):
            a=self.l[i]
            #print(a.val)
            while(a.next!=None):
                a=a.next
                #print(a.val)
            #print()
    
class treeMEX:
    def __init__(self,n,adj):
        self.a=[-1]*n
        self.b=[] #perm secondary list
        self.c=[] #perm main list
        self.d=[] #test list
        self.perm([i for i in range(1,n+1)],n,adj)
    def MEX(self,i,x):  #x link to the head node of nearest neighbours to current element
        k=0
        if(x!=None):
            if(self.a[x.val-1]>=0 and self.a[x.val-1]==k):
                k+=1
            while(x.next!=None):
                x=x.next
                if(self.a[x.val-1]>=0 and self.a[x.val-1]==k):
                    k+=1
        #print(str(i)+" "+str(k))
        self.a[i]=k
    def perm(self,a,n,adj):
        if(len(a)==0):
            self.a=[-1]*n
            v=list(self.b)
            #print(v)
            #print(v)
            #print(list(self.b))
            for i in range(n):
                self.MEX(v[i]-1,adj.l[v[i]-1])
            #self.a=[self.MEX(v[i]-1,adj.l[v[i]-1]) for i in range(n)]
            if(self.a not in self.c):
                self.c.append(list(self.a))
                self.d.append(v)
        else:
            for i in range(len(a)):
                self.b.append(a[i])
                self.perm(a[:i]+a[i+1:],n,adj)
                self.b.pop()

t=int(input())
for i in range(t):
    n=int(input())
    adj=adjList(n)
    for j in range(n-1):
        x=input()
        adj.addVertex(x)
    adj.see()
    mex=treeMEX(n,adj)
    #print(mex.d)
    #print(mex.c)
    print(int(len(mex.c)%(10e9+7)))
    