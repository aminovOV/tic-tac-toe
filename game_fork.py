# ============================================
import os
from random import randint


# ============================================
class Field:
    def __init__(self, field=None):
        self.field = field
        self.field = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def start_field(self, field=None):
        self.field = field
        self.field = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def set_field(self, index, value):
        self.field[index] = value

    def get_field(self):
        return self.field


# ============================================
class FieldDisplay(Field):
    def __init__(self):
        super().__init__()

    def display_field(self):
        print(f"               {' | '.join(self.get_field()[0:3])}")
        print("              -----------")
        print(f"               {' | '.join(self.get_field()[3:6])}")
        print("              -----------")
        print(f"               {' | '.join(self.get_field()[6:9])}")


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


# ============================================
class GameScreen(FieldDisplay, Counter):
    def __init__(self):
        super().__init__()

    def get_screen(self):
        os.system('cls||clear')
        print(f"------------------------------------\n         КРЕСТИКИ - НОЛИКИ\n"
              f"------------------------------------\n")
        print(f"  ▬▬▬▬▬▬▬▬\n    СЧЕТ  \n  ▬▬▬▬▬▬▬▬\n\n  Вы: {self.get_user_points()}\n  "
              f"Бот: {self.get_bot_points()}\n\n")
        self.display_field()


# ============================================
class StartScreen(GameScreen):
    def __init__(self):
        super().__init__()

    def start_screen(self):
        self.get_screen()
        print(input("\n\n\nДля начала игры нажмите Enter"))
        os.system('cls||clear')


# ============================================
class WinLines(Field):
    def __init__(self):
        super().__init__()

    def win_lines(self):
        self.lines = [self.get_field()[0:3],
                      self.get_field()[3:6],
                      self.get_field()[6:9],
                      self.get_field()[0:7:3],
                      self.get_field()[1:8:3],
                      self.get_field()[2:9:3],
                      self.get_field()[0:9:4],
                      self.get_field()[2:7:2]]
        return self.lines


# ============================================
def priority_move():
    priority = randint(0, 1)
    return priority


# ============================================
class User(GameScreen):
    def __init__(self):
        super().__init__()

    def user_move(self):
        while True:
            position = input("\n\nВведите номер клетки и нажмите Enter: ")
            self.get_screen()
            if not position:
                self.get_screen()
                print("\nВы не ввели номер клетки")
                continue
            position = int(position)
            if position < 1 or position > 9:
                self.get_screen()
                print("\nНомер клетки вне диапазона игрового поля")
                continue
            if self.get_field()[position - 1] == str(position):
                self.set_field(position - 1, "x")
                break
        return self.get_field()


# ============================================
class Bot(Field):
    def __init__(self):
        super().__init__()

    def bot_move(self):
        while True:
            rand = randint(0, 8)
            if self.get_field()[rand] != '0' and self.get_field()[rand] != 'x':
                self.set_field(rand, '0')
                break
        return self.get_field()


# ============================================
class EndGame(StartScreen):
    def __init__(self):
        super().__init__()

    def end(self):
        while True:
            next_game_request = input("""
        Если хотите сыграть еще раз, 
        введите 'y' и нажмите Enter
        Если хотите выйти, 
        введите 'n' нажмите Enter: """)
            if next_game_request == 'y':
                start.game()
            elif next_game_request == 'n':
                os.system('cls||clear')
                print("\nВсего хорошего\n")
                exit()
            elif not next_game_request:
                self.get_screen()
                print("\nВы ничего не ввели\n")
            else:
                self.get_screen()
                print("\nВы ввели неверную букву\n")
                continue


# ============================================
class WinCheck(WinLines, EndGame):
    def __init__(self):
        super().__init__()

    def win_check(self):
        while True:
            if any(line == ['x', 'x', 'x'] for line in self.win_lines()):
                self.get_screen()
                self.set_user_points()
                self.start_field()
                print("\n\n\nПобеда за Вами! Skynet уничтожен!")
                self.end()
            elif any(line == ['0', '0', '0'] for line in self.win_lines()):
                self.get_screen()
                self.set_bot_points()
                self.start_field()
                print("\n\n\nПобедил искусственный интеллект!")
                self.end()
            elif all(cells == 'x' or cells == '0' for cells in self.get_field()):
                self.get_screen()
                self.start_field()
                print("\n\n\nНичья!")
                self.end()
            else:
                break


# ============================================
class Game(WinCheck, User, Bot):
    def game(self):
        self.start_screen()
        if priority_move() == 1:
            self.get_screen()
            print("\nПервый ход Ваш")
            self.user_move()
        while True:
            self.get_screen()
            self.bot_move()
            self.get_screen()
            print("\nБот сходил\n")
            print("\nСледующий ход Ваш")
            self.win_check()
            self.user_move()
            self.win_check()


# ============================================
if __name__ == "__main__":
    start = Game()
    start.game()
