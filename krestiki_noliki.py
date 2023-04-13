field = [
         ["-","-","-"],
         ["-","-","-"],
         ["-","-","-"]
         ]

def game_board():

    print("  0 1 2 ")
    for i in range(3):
        print(str(i), *field[i])

def ask():
    while True:
        index = input("введите номер координат 'X , Y': ").split()
        if len(index) != 2:
            print("нужны две координаты")
            continue
        if not (index[0].isdigit() and index[1].isdigit()):
            print("нужны числа")
            continue
        x = int(index[1])
        y = int(index[0])
        if not (0 <= x <= 2 and 0 <= y <= 2):
            print("введите верные координаты с интервалом от 0 до 2 ")
            continue
        if field[x][y] != "-":
            print(" Клетка занята! ")
            continue
        return x, y

def win():
    win_1 = False
    if field[0][0] == "x" and field[0][1] == "x" and field[0][2] == "x":
        print("победа X")
        win_1 = True
    if field[1][0] == "x" and field[1][1] == "x" and field[1][2] == "x":
        win_1 = True
        print("победа X")
    if field[2][0] == "x" and field[2][1] == "x" and field[2][2] == "x":
        win_1 = True
        print("победа X")

    if field[0][0] == "0" and field[0][1] == "0" and field[0][2] == "0":
        print("победа 0")
        win_1 = True
    if field[1][0] == "0" and field[1][1] == "0" and field[1][2] == "0":
        win_1 = True
        print("победа 0")
    if field[2][0] == "0" and field[2][1] == "0" and field[2][2] == "0":
        win_1 = True
        print("победа 0")

    if field[0][0] == "x" and field[1][0] == "x" and field[2][0] == "x":
        print("победа X")
        win_1 = True
    if field[0][1] == "x" and field[1][1] == "x" and field[2][1] == "x":
        win_1 = True
        print("победа X")
    if field[0][2] == "x" and field[1][2] == "x" and field[2][2] == "x":
        win_1 = True
        print("победа X")

    if field[0][0] == "0" and field[1][0] == "0" and field[2][0] == "0":
        print("победа 0")
        win_1 = True
    if field[0][1] == "0" and field[1][1] == "0" and field[2][1] == "0":
        win_1 = True
        print("победа 0")
    if field[0][2] == "0" and field[1][2] == "0" and field[2][2] == "0":
        win_1 = True
        print("победа 0")

    if field[0][0] == "x" and field[1][1] == "x" and field[2][2] == "x":
        print("победа X")
        win_1 = True
    if field[0][2] == "x" and field[1][1] == "x" and field[2][0] == "x":
        win_1 = True
        print("победа X")

    if field[0][0] == "0" and field[1][1] == "0" and field[2][2] == "0":
        print("победа 0")
        win_1 = True
    if field[0][2] == "0" and field[1][1] == "0" and field[2][0] == "0":
        win_1 = True
        print("победа 0")


    return win_1


i = 1
count = 1
while i < 10:
    game_board()
    win_1 = win()
    if win_1:
        break
    if count % 2 == 1:
        print("Ходит Х")
    else:
        print("ходит 0")
    x,y = ask()
    print(x,y)
    if count % 2 == 1:
        field[x][y] = "x"
    else:
        field[x][y] = "0"
    i += 1
    count +=1
else:
    print("нчиья")