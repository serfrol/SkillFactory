board = list(range(1,10))

#def wantsToPlay(func):
#    def wrapper():
#        if wants:
#            print("Вы решили поиграть...")
#            func()
#        else:
#            print("Вы решили не играть...")
#    return wrapper

def drawBoard(board):
    i = 0
    print("  |",i,"|",i+1,"|",i+2)
    print("--------------")
    for j in range(3):
        print(j,"|",board[0+j*3],"|",board[1+j*3],"|",board[2+j*3])
    print("--------------")

def playerInput(xo):
    correct = False
    while not correct:
        answer = input(f"Куда хотите поставить {xo}? ")
        try:
            answer = int(answer)
        except:
            print("Вы ввели не цифру!")
            continue
        if 1<=answer<=9:
            if str(board[answer-1]) != ("x" or "o"):
                board[answer-1] = xo
                correct = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Введите цифру (1-9)!")

def checkWin(board):
    win = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for i in win:
        if board[i[0]] == board [i[1]] == board [i[2]]:
            return board[i[0]]
    return False

#@wantsToPlay
def game(board):
    count = 0
    win = False
    while not win:
        drawBoard(board)
        if count % 2 == 0:
            playerInput("x")
            count += 1
        else:
            playerInput("o")
            count += 1
        if checkWin(board):
            win = True
            if count % 2 == 0:
                print("Победили нолики!")
            else:
                print("Победили крестики!")
        elif count == 9:
            win = True
            print("Ничья")

#yesno = str(input("Введите Y, если хотите сыграть в крестики-нолики. "))
#wants = yesno == "Y"
game(board)