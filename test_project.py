def greet():
    print("  Добро пожаловать  ")
    print("      в игру       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода данных: x y ")
    print(" x - это номер строки  ")
    print(" y - это номер столбца ")

def show():
    print()
    print("    0  1  2  ")
    for i in range(3):
        print(f"{i}{field[i][0]} {field[i][1]} {field[i][2]}")

def ask():
    while True:
        turn = input(" Ваш ход: ").split()

        x, y = turn

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 <= x <= 2 and 0 <= y <= 2:
            if field[x][y] == " ":
                return x, y
            else:
                print(" Клетка занята ")
        else:
            print(" Проверьте правильность ввода данных ")

    return x, y

def check_win():
    win_turn = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for turns in win_turn:
        symbols = []
        for c in turns:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False

greet()
field = [[" ", " ", " "] for i in range(3)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "  X"
    else:
        field[x][y] = "  0"
    if check_win():
        break
    if count == 9:
        print(" Ничья!")
        break