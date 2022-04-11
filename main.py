print("Tic Tac Toe\n")

winConditions=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

indexArr = [1,2,3,4,5,6,7,8,9]

def printBoard():
    print(indexArr[0],'|',indexArr[1],'|',indexArr[2])
    print('--|---|--')
    print(indexArr[3],'|',indexArr[4],'|',indexArr[5])
    print('--|---|--')
    print(indexArr[6],'|',indexArr[7],'|',indexArr[8])

xArr=[]
oArr=[]

flag = 1
while(True):
    if flag==1:
        printBoard()
        print("Player X, it is your turn. Enter the grid number where you would like to place the mark: ")
        xMark = int(input())
        print("\n")
        xArr.append(xMark)
        indexArr[xMark-1]='X'
        xArr.sort()
        flag =2
    else:
        printBoard()
        print("Player O, it is your turn. Enter the grid number where you would like to place the mark: ")
        print("\n")
        oMark=int(input())
        oArr.append(oMark)
        indexArr[oMark-1]='O'
        oArr.sort()
        flag = 1
    if (xArr[0:3] in winConditions) or (oArr[0:3] in winConditions):
        if flag==1:
            print("Player O wins")
        else:
            print("Player X wins")
        break
