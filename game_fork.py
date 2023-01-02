# ============================================
import os
from random import randint


# ============================================
class Field:
    def __init__(self, game_field=None):
        self.game_field = game_field
        self.game_field = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def start_field(self, game_field=None):
        self.game_field = game_field
        self.game_field = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def set_field(self, index, value):
        self.game_field[index] = value

    def get_field(self):
        return self.game_field


field = Field()


# ============================================
class Counter:
    def __init__(self) -> None:
        pass

    user_points = 0
    bot_points = 0

    def set_user_points(self):
        self.user_points += 1

    def get_user_points(self):
        return self.user_points

    def set_bot_points(self):
        self.bot_points += 1

    def get_bot_points(self):
        return self.bot_points


count = Counter()


# ============================================
class Static:
    def __init__(self):
        pass

    @staticmethod
    def display():
        print(f"               {' | '.join(field.get_field()[0:3])}")
        print("              -----------")
        print(f"               {' | '.join(field.get_field()[3:6])}")
        print("              -----------")
        print(f"               {' | '.join(field.get_field()[6:9])}")

    @staticmethod
    def get_screen():
        os.system('cls||clear')
        print(f"------------------------------------\n         КРЕСТИКИ - НОЛИКИ\n"
              f"------------------------------------\n")
        print(f"  ▬▬▬▬▬▬▬▬\n    СЧЕТ  \n  ▬▬▬▬▬▬▬▬\n\n  Вы: {count.get_user_points()}\n  "
              f"Бот: {count.get_bot_points()}\n\n")
        Static.display()

    @staticmethod
    def start_screen():
        Static.get_screen()
        print(input("\n\n\nДля начала игры нажмите Enter"))
        os.system('cls||clear')

    @staticmethod
    def win_lines():
        lines = [field.get_field()[0:3],
                 field.get_field()[3:6],
                 field.get_field()[6:9],
                 field.get_field()[0:7:3],
                 field.get_field()[1:8:3],
                 field.get_field()[2:9:3],
                 field.get_field()[0:9:4],
                 field.get_field()[2:7:2]]
        return lines

    @staticmethod
    def priority_move():
        priority = randint(0, 1)
        return priority

    @staticmethod
    def end_game():
        while True:
            next_game_request = input("""
            Если хотите сыграть еще раз, 
            введите 'y' и нажмите Enter
            Если хотите выйти, 
            введите 'n' нажмите Enter: """)
            if next_game_request == 'y':
                Game.start()
            elif next_game_request == 'n':
                os.system('cls||clear')
                print("\nВсего хорошего\n")
                exit()
            elif not next_game_request:
                Static.get_screen()
                print("\nВы ничего не ввели\n")
            else:
                Static.get_screen()
                print("\nВы ввели неверную букву\n")
                continue

    @staticmethod
    def win_check():
        while True:
            if any(line == ['x', 'x', 'x'] for line in Static.win_lines()):
                Static.get_screen()
                count.set_user_points()
                field.start_field()
                print("\n\n\nПобеда за Вами! Skynet уничтожен!")
                Static.end_game()
            elif any(line == ['0', '0', '0'] for line in Static.win_lines()):
                Static.get_screen()
                count.set_bot_points()
                field.start_field()
                print("\n\n\nПобедил искусственный интеллект!")
                Static.end_game()
            elif all(cells == 'x' or cells == '0' for cells in field.get_field()):
                Static.get_screen()
                field.start_field()
                print("\n\n\nНичья!")
                Static.end_game()
            else:
                break


# ============================================
class User:
    def __init__(self):
        pass

    @staticmethod
    def move():
        while True:
            position = input("\n\nВведите номер клетки и нажмите Enter: ")
            Static.get_screen()
            if not position or not position.isdigit():
                Static.get_screen()
                print("\nВы не ввели номер клетки")
                continue
            position = int(position)
            if position < 1 or position > 9:
                Static.get_screen()
                print("\nНомер клетки вне диапазона игрового поля")
                continue
            if field.get_field()[position - 1] == str(position):
                field.set_field(position - 1, "x")
                break
        return field.get_field()


# ============================================
class Bot:
    def __init__(self):
        pass

    @staticmethod
    def move():
        while True:
            rand = randint(0, 8)
            if field.get_field()[rand] != '0' and field.get_field()[rand] != 'x':
                field.set_field(rand, '0')
                break
        return field.get_field()


# ============================================
class Game:
    def __init__(self):
        pass

    @staticmethod
    def start():
        Static.start_screen()
        if Static.priority_move() == 1:
            Static.get_screen()
            print("\nПервый ход Ваш")
            User.move()
        while True:
            Static.get_screen()
            Bot.move()
            Static.get_screen()
            print("\nБот сходил\n")
            print("\nСледующий ход Ваш")
            Static.win_check()
            User.move()
            Static.win_check()


# ============================================
if __name__ == "__main__":
    Game.start()
