import random
import os


game_field = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
user_points = 0
bot_points = 0


def game_screen():
    os.system('cls||clear')
    print(f"------------------------------------\n         КРЕСТИКИ - НОЛИКИ\n"
          f"------------------------------------\n")
    print(f"  ▬▬▬▬▬▬▬▬\n    СЧЕТ  \n  ▬▬▬▬▬▬▬▬\n\n  Вы: {user_points}\n  Бот: {bot_points}\n\n")
    print(f"               {' | '.join(game_field[0:3])}")
    print("              -----------")
    print(f"               {' | '.join(game_field[3:6])}") 
    print("              -----------")
    print(f"               {' | '.join(game_field[6:9])}") 


def start_screen():
    game_screen()
    print(input("\n\n\nДля начала игры нажмите Enter"))
    os.system('cls||clear')


def priority_move():
    priority = random.randint(0, 1)
    return priority


def bot():
    while True:
        rand = random.randint(0, 8)
        if game_field[rand] != '0' and game_field[rand] != 'x':
            game_field[rand] = '0'
            break
    return game_field


def user():
    while True:
        position = input("\n\nВведите номер клетки и нажмите Enter: ")
        if not position:
            game_screen()
            print("\nВы не ввели номер клетки")
            continue
        position = int(position)
        if position < 1 or position > 9:
            game_screen()
            print("\nНомер клетки вне диапазона игрового поля")
            continue
        if game_field[position-1] == str(position):
            game_field[position-1] = "x"
            break
    return game_field


def win_check():
    global game_field
    global user_points
    global bot_points
    win_lines = [game_field[0:3],
                 game_field[3:6],
                 game_field[6:9],
                 game_field[0:7:3],
                 game_field[1:8:3],
                 game_field[2:9:3],
                 game_field[0:9:4],
                 game_field[2:7:2]]
    while True:
        if any(line == ['x', 'x', 'x'] for line in win_lines):
            game_screen()
            user_points += 1
            game_field = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            print("\n\n\nПобеда за Вами! Skynet уничтожен!")
            end_game()
        elif any(line == ['0', '0', '0'] for line in win_lines):
            game_screen()
            bot_points += 1
            game_field = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            print("\n\n\nПобедил искусственный интеллект!")
            end_game()
        elif all(cells == 'x' or cells == '0' for cells in game_field):
            game_screen()
            game_field = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            print("\n\n\nНичья!")
            end_game()
        else:
            break
            # return


def end_game():
    while True:
        next_game_request = input("""
    Если хотите сыграть еще раз, 
    введите 'y' и нажмите Enter
    Если хотите выйти, 
    введите 'n' нажмите Enter: """)
        if next_game_request == 'y':
            game()
        elif next_game_request == 'n':
            os.system('cls||clear')
            print("\nВсего хорошего\n")
            exit()
        elif not next_game_request:
            game_screen()
            print("\nВы ничего не ввели\n")
        else:
            game_screen()
            print("\nВы ввели неверную букву\n")
            continue


def game():
    start_screen()
    if priority_move() == 1:
        game_screen()
        print("\nПервый ход Ваш")
        user()
    while True:
        game_screen()
        bot()
        game_screen()
        print("\nБот сходил\n")
        print("\nСледующий ход Ваш")
        win_check()
        user()
        win_check()


game()
