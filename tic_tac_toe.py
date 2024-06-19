import colorama
def draw_board(a):
    print(" | ".join(a[0:3]))
    print(" ___ " * 2)
    print(" | ".join(a[3:6]))
    print(" ___ " * 2)
    print(" | ".join(a[6:9]))


def createboard():
    d = []
    for i in range(1, 10):
        i = str(i)
        d.append(i)
    return d


def check(n, doska):
    if n.isdigit() == False:
        print("Это не цифра")
        return False
    elif int(n) < 1 or int(n) > 9:
        print("Такой ячейки нет")
        return False
    elif doska[int(n) - 1] == 'x' or doska[int(n) - 1] == '0':
        print("Эта ячейка занята")
        return False
    else:
        return True


def check_win(board):
    q = [[0, 4, 8], [2, 4, 6], [0, 1, 2], [0, 3, 6], [6, 7, 8], [2, 5, 8], [3, 4, 5], [1, 4, 7]]
    for e in q:
        if board[e[0]] == board[e[1]] == board[e[2]]:
            print(board[e[0]],"победил")
            return True
    else:
        for i in board:
            if i != "x" and i != "0":
                return False
        else:
            print("ничья")
            return True


def main():
    x = 'x'
    o = '0'
    doska = createboard()
    draw_board(doska)
    symbol = input(("Выберите символ: 'x' или '0' "))
    while symbol != o and symbol != x:
        symbol = input(("ошибка, выберите символ: 'x' или '0' "))
    while True:
        if symbol == x:
            print("Ваш знак: х")
        elif symbol == o:
            print("Ваш знак: 0")
        n = input(("Выберите номер ячейки от 1 до 9 "))
        while check(n, doska) == False:
            n = input(("Выберите номер ячейки от 1 до 9 "))

        doska[int(n) - 1] = symbol
        draw_board(doska)
        if symbol == x:
                symbol = o
        elif symbol == o:
                symbol = x
        if check_win(doska) == True:
            break
main()
