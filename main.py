import random
import time

#Постоянные переменные
symbols = ["X", "O"] #Крестик и нолик для проверки
board = [1, 2, 3, 4, 5, 6, 7, 8, 9] #Список значений клеток игрового поля
WinCon = False #Условие выигрыша
Players = [] #Список игроков
Player1 = "" #Имя первого игрока
Player2 = "" #Имя второго игрока
PlayFirst = "" #Кто ходит первым
PlaySecond = "" #Кто ходит вторым
PlayFirstSymb = "" #Символ первого игрока
PlaySecondSymb = "" #Символ второго игрока
WhoTurn = "" # чей ход
TurnSymbol = "" #Символ хода
Winner = "" #Победитель
StepCounter = 0 #Счетчик ходов

#Вывод игровое поле
def OpenBoard():
    global board
    print("\n\t",board[0],"|",board[1],"|", board[2])
    print("\t","----------")
    print("\n\t",board[3],"|",board[4],"|", board[5])
    print("\t","----------")
    print("\n\t",board[6],"|",board[7],"|", board[8], "\n")

#Проверка состояния выигрыша
def WinCon(board):
    if board[0] == board [1] == board[2]:
        return True
    elif board[3] == board [4] == board[5]:
        return True
    elif board[6] == board [7] == board[8]:
        return True
    elif board[0] == board [3] == board[6]:
        return True
    elif board[1] == board [4] == board[7]:
        return True
    elif board[2] == board [5] == board[8]:
        return True
    elif board[0] == board [4] == board[8]:
        return True
    elif board[2] == board [4] == board[6]:
        return True
    else:
        return False

#Проверка ответа Да/Нет
def YNCheck(Answer):
    if Answer in (1,2):
        return True
    else:
        print("Вы ввели некорректное число! Нужно написать 1 или 2")
        return False

#Проверка выбора клетки
def ChoiceCheck(PlayChoice):
    try:
        if board[PlayChoice] == symbols[0]:
            print("Вы ввели неправильное число или уже занятое поле!")
            return False
        elif board[PlayChoice] == symbols[1]:
            print("Вы ввели неправильное число или уже занятое поле!")
            return False
        else:
            return True
    except IndexError:
        print("Таких полей нет!")

#Начальная инструкция
def Intro():
    print("Дорогие игроки! Приветствуем вас в игре `Крестики-нолики`! ")
    print("Правила игры просты: играют два игрока, которые жребием решают, ставят они на игровое поле крестик либо нолик.")
    print("Игроки ходят по очереди, выбирая номер поля, на котором ставится их символ.")
    print("Игрок собравший на поле ряд из трех своих символов по диагонали, горизонтали или вертикали - побеждает.")
    print("Ну что, начнём игру? (1 - Да, 2 - Нет)" )
    AnswIntro = 0
    while AnswIntro not in (1,2):
        try:
            AnswIntro = int(input())
            YNCheck(AnswIntro)
        except ValueError:
            print("Буквы вводить нельзя! Введите цифры 1 или 2")
        if AnswIntro == 1:
            print("Погнали!")
        elif AnswIntro == 2:
            print("До скорой встречи!")
            exit()

#Задаём имена игроков
def PlayerNames():
    global Player1, Player2
    Player1 = input("Введите имя первого игрока:")
    Player2 = input("Введите имя второго игрока:")
    Players.append(Player1)
    Players.append(Player2)

#Выбираем кто играет первый
def WhoPlayFirst(Players):
    global Player1, Player2, PlayFirst, PlaySecond
    print("Cейчас монетка решит, кто ходит первым")
    PlayFirst = random.choice(Players)
    point = "Монетка крутится."
    for i in range(1,5):
        time.sleep(1)
        print(point)
        point += "."
    print("Первым ходит....", PlayFirst)
    if PlayFirst == Players[0]:
       PlaySecond = Players[1]
    else:
       PlaySecond = Players[0]
    print("Ну а вторым ходит", PlaySecond)

#Выбираем крестик ставим или нолик
def CresorZero():
    global PlayFirst, PlayFirstSymb, PlaySecondSymb
    print(PlayFirst, "Вы хотите играть крестиками или ноликами?")
    print("Введите цифру: 1 - Крестики, 2 - Нолики")
    AnswCZ = 0
    while AnswCZ not in (1, 2):
        try:
            AnswCZ = int(input())
            YNCheck(AnswCZ)
        except ValueError:
            print("Буквы вводить нельзя! Введите цифры 1 или 2")
    if AnswCZ == 1:
        PlayFirstSymb = "X"
        PlaySecondSymb = "O"
    else:
        PlayFirstSymb = "O"
        PlaySecondSymb = "X"
    print(f"Поздравляю! {PlayFirst} играет - {PlayFirstSymb}, a {PlaySecond} играет - {PlaySecondSymb}")

#Поздравляем победителя
def gratz():
    if WinCon(board) == True:
        print("Поздравляю", Winner, "вы победили!")
    else:
        pass

#Запуск игры
def InitGame():
    global WhoTurn, TurnSymbol, Winner, StepCounter
    PlayerNames()
    WhoPlayFirst(Players)
    CresorZero()
    WhoTurn = PlayFirst
    TurnSymbol = PlayFirstSymb
    print("Итак, дорогие", PlayFirst, "и", PlaySecond, "пора начинать!")
    while WinCon(board) is not True:
        if StepCounter == 9:
            print("Поздравляю с боевой ничьёй!")
            break
        Turn()
        StepCounter +=1
    gratz()

#Ход
def Turn():
    global WhoTurn, TurnSymbol, board, Winner
    print(WhoTurn, "ваш ход, вы ставите", TurnSymbol)
    OpenBoard()
    ChoCheck = False
    while ChoCheck is not True:
        try:
            PlayChoice = int(input("Введите номер незанятого квадрата куда вы хотите поставить свой символ?"))
            PlayChoice -=1
            ChoCheck = ChoiceCheck(PlayChoice)
        except ValueError:
            print("Буквы вводить нельзя! Введите номер незанятого квадрата!")
    board[PlayChoice] = TurnSymbol
    OpenBoard()
    if WinCon(board)== True:
        Winner = WhoTurn
    if WhoTurn == PlayFirst:
        WhoTurn = PlaySecond
        TurnSymbol = PlaySecondSymb
    else:
        WhoTurn = PlayFirst
        TurnSymbol = PlayFirstSymb
Intro()
InitGame()