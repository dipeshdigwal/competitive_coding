
class treeMEX:
    def __init__(self, n, adj):
        self.a = [-1]*n
        self.b = []  # perm secondary list
        self.c = []  # perm main list
        self.d = []  # test list
        self.perm([i for i in range(1, n+1)], n, adj)

    def MEX(self, i, x):  # x link to the head node of nearest neighbours to current element
        k = 0
        if(x != None):
            if(self.a[x.val-1] >= 0 and self.a[x.val-1] == k):
                k += 1
            while(x.next != None):
                x = x.next
                if(self.a[x.val-1] >= 0 and self.a[x.val-1] == k):
                    k += 1
        #print(str(i)+" "+str(k))
        self.a[i] = k

    def perm(self, a, n, adj):
        if(len(a) == 0):
            self.a = [-1]*n
            v = list(self.b)
            # print(v)
            # print(v)
            # print(list(self.b))
            for i in range(n):
                self.MEX(v[i]-1, adj.l[v[i]-1])
            #self.a=[self.MEX(v[i]-1,adj.l[v[i]-1]) for i in range(n)]
            if(self.a not in self.c):
                self.c.append(list(self.a))
                self.d.append(v)
        else:
            for i in range(len(a)):
                self.b.append(a[i])
                self.perm(a[:i]+a[i+1:], n, adj)
                self.b.pop()
