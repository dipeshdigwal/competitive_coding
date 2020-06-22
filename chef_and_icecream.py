def can_icecream_be_served(A):
    shops_money = [0]*4  # 0:Rs 5 , 1:Rs 10 , 2:Rs 15 , 3:Total
    for i in A:
        balance = int(i)-5
        if(balance == 0):
            shops_money[0] += 1
        elif(balance == 5):
            if(shops_money[0] < 1):
                return("NO")
            else:
                shops_money[0] -= 1
                shops_money[1] += 1
        else:
            if(shops_money[1] < 1):
                if(shops_money[0] < 2):
                    return("NO")
                else:
                    shops_money[0] -= 2
                    shops_money[2] += 1
            else:
                shops_money[1] -= 1
                shops_money[2] += 1
            

    return("YES")


T = int(input())
for i in range(T):
    N = int(input())
    A = input().split(" ")
    print(can_icecream_be_served(A))
