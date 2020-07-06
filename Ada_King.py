def displayBoard(board):
    for i in board:
        print(i)


def adaKing2(K):
    if(K==64):
        board=[]
        for i in range(8):
            if(i!=7):
                board.append("."*8)
            else:
                board.append("O"+("."*7))
        return(board)
    board = []
    sqr = [i*i for i in range(1, 9)]
    for i in range(len(sqr)):
        if(sqr[i] > K):
            n = i
            r = K-(n*n)
            x = r-n
            break
    if(r == 0):
        for i in range(8):
            if(i < (7-n)):
                board.append("."*8)
            elif(i == (7-n)):
                board.append("X"*(n+1)+("."*(7-n)))
            elif(i < 7):
                board.append(("."*(n))+"X"+("."*(7-n)))
            else:
                board.append("O"+("."*(n-1))+"X"+("."*(7-n)))
    elif(r < (n+1)):
        for i in range(8):
            if(i < (6-n)):
                board.append("."*8)
            elif (i == (6-n)):
                board.append(("X"*(r+1))+("."*(7-r)))
            elif (i == (7-n)):
                board.append(("."*r)+("X"*(n-r+1))+("."*(7-n)))
            elif(i < 7):
                board.append(("."*n)+"X"+("."*(7-n)))
            else:
                board.append("O"+("."*(n-1))+"X"+("."*(7-n)))
    else:
        for i in range(8):
            if(i < (6-n)):
                board.append("."*8)
            elif(i == (6-n)):
                board.append("X"*(n+2)+("."*(6-n)))
            elif(i < (7-n+x)):
                if(i<=x):
                    board.append(("."*(n+1)))
                else:    
                    board.append(("."*(n+1))+"X"+("."*(6-n)))
            elif (i == (7-n+x)):
                if(i==x):
                    if(i!=7):
                        board.append(("."*n)+"X")
                    else:
                        board.append("O"+("."*(n-1))+"X")
                    
                elif(i==7):
                    board.append("O"+("."*(n-1))+"XX"+("."*(6-n)))
                
                else:
                    board.append(("."*n)+"XX"+("."*(6-n)))
            else:
                if(i==7):
                    board.append("O"+("."*(n-1))+"X"+("."*(7-n)))
                else:
                    board.append(("."*(n))+"X"+("."*(7-n)))
    return(board)


T = int(input())
for i in range(T):
    K = int(input())
    displayBoard(adaKing2(K))
