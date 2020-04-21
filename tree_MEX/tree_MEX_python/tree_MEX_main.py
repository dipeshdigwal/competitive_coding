t = int(input())
for i in range(t):
    n = int(input())
    adj = adjList(n)
    for j in range(n-1):
        x = input()
        adj.addVertex(x)
    adj.see()
    mex = treeMEX(n, adj)
    # print(mex.d)
    # print(mex.c)
    print(int(len(mex.c) % (10e9+7)))
