#
# Игра крестики нолики
# ** Автор Ринчино Булат (https://github.com/Bulatr/game-krestiki.git)

# количество клеток
board_size = 3

# Игровое поле
board = [1,2,3,4,5,6,7,8,9]

symbols = ["x","o"]

# функция выводит игровое поле
def draw_board():
    print("_"*4*board_size)
    for i in range(board_size):
        print( (" " * 3 + "|") * 3)
        print(" "+str( board[i*3] )+" | "+str( board[1+i*3] )+" | "+str( board[2+i*3] )+" |")
        print( ("_" * 3 + "|") * 3)
    pass

# функция которая делает ход и записывает в список символ current_player
def select_step(index, current_player):
    index = int(index)
    if (index < 1 or index > 9 or board[index-1] in ("x","o")):
        return False
    else:
        board[index-1] = current_player
        return True

# Фунция выбора первого игрока
def select_first_gamer():
    flag_continue = True
    while flag_continue:
        print("Выберите игрока который пойдет первым")
        first_player = input("x или o: ")
        if first_player not in symbols:
            print("Выбран неверный символ")
            continue
        else:
            return first_player

# выбор хода
def step_gamer(current_player, board, symbols):
    max_step = len(board)
    symbols = symbols
    while True:
        step_g = input(f"Ходит игрок {current_player}. Введите номер поля (от 1 до {max_step}), 0 - выход: ")
        # на ввод числа
        try:
            if int(step_g) in board:
                return step_g

            else:
                if int(step_g) == 0:
                    return False
                print(f"Введен неправильный символ. Введите номер поля (от 1 до {max_step})")
                continue
        except:
            print("Введен неправильный символ")
            continue

# Функция проверки победы
def check_win():
    win = False
    #  Выйгрышные комбинации
    win_combinations = (
        (0,1,2),(3,4,5),(6,7,8), # Гориз линии
        (0,3,6),(1,4,7),(2,5,8), # Верт линии
        (0,4,8),(2,4,6) # Диагонали
    )
    for position in win_combinations:
        if (board[position[0]] == board[position[1]] and board[position[1]] == board[position[2]]):
            win = board[position[0]]
            return win
    return win

# Основная функция
def main_game():
    print("Добро пожаловать в игру крестики и нолики")
    draw_board()
    # шаг игры
    step = 1
    if step == 1:
        # Текущий игрок
        current_player = select_first_gamer()

    # Если выбрано верно
    if current_player:
        # создаем цикл пока шаг игры < 10 и check_win == false
        while ( step < 10 ) and check_win() == False:
            # Делаем ход
            index = step_gamer(current_player, board, symbols)
            print(index)
            # Пользователь ввел данные успешно (числа от 1 до 9)
            if index:
                select_step(index, current_player)
                print(board)
                # Меняем сторону
                if current_player == "x":
                    current_player = "o"
                else:
                    current_player = "x"
                draw_board()
                step += 1

            else:
                print("Игра окончена")
                break
        if step == 10:
            print("Ничья")
        else:
            print(f"Выйграл {check_win()}")
    else:
        select_first_gamer()
    pass

# запуск главной функции
main_game()