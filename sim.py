mod=10e9+7
class swap:
    def case1(self,a,s):
        for i in range(a[1],a[2]):
            s[i]=a[3]
        #return(s)
    def case2(self,a,s):
        for i in range(a[1],a[2]):
            if(s[i]=="A"):
                x=(a[3]-a[4]+mod)%mod
                y=(a[3]+a[4])%mod
            else:
                x=(a[3]+a[4])%mod
                y=(a[4]-a[3]+mod)%mod
            a[3]=x
            a[4]=y
def main():
    t=int(input())
    n=int(input())
    s=input()
    q=int(input())
    cl=swap()
    for i in range(q):
        st=input().split()
        print(st)
        if(st[0]==1):
            cl.case1(st,s)
        else:
            cl.case2(st,s)
            print(str(a[3])+" "+str(a[4])+"\n")

main()