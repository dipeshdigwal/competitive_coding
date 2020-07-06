########check if a number is a prime number######
########return 1 if a number is prime number else 0#####
def prime(x):
    for i in range(2, int(x/2)+1):
        if(x % i == 0):
            return(0)
    return(1)

########swap two adjacent Puzzle boxes#######
########      A:Puzzle Matrix         #######
########      C1:Coordinates of first box####
########      C2:Coordinates of second box###


def swapper(A, C1, C2):
    x = A[C1[0]][C1[1]]
    A[C1[0]][C1[1]] = A[C2[0]][C2[1]]
    A[C2[0]][C2[1]] = x
    return(A)


def indexChooser(A):
    Steps=0
    for i in range(3):
        for j in range(3):
            if

t = int(input())
for i in range(t):
    input()
    Puzzle = []
    for j in range(3):
        Puzzle.append(input().split(" "))
