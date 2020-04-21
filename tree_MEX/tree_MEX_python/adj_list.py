class adjList:
    def __init__(self, n):
        self.l = [linkList(i) for i in range(1, n+1)]

    def addEle(self, i, j):
        x = self.l[i-1]
        if(x != None):
            while(x.next != None):
                x = x.next
            x.next = linkList(j)

    def addVertex(self, a):
        x = a.split(" ")
        i = int(x[0])
        j = int(x[1])
        self.addEle(i, j)  # back linking not happening....
        self.addEle(j, i)

    def see(self):
        for i in range(len(self.l)):
            a = self.l[i]
            # print(a.val)
            while(a.next != None):
                a = a.next
                # print(a.val)
            # print()
