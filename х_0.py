# import tkinter
#
#
# def draw_area():
#     for i in area:
#         print(*i)
#     print()
#
#
# area =[['*', '*','*'], ['*', '*','*'],['*', '*','*']]
# print('Добро пожаловать в игру')
# print('-----------------------')
# draw_area()
# for turn in range(1, 10):
#     print(f'Ход: {turn}')
#     if turn % 2 == 0:
#         turn_char = '0'
#         print('Ходят нолики')
#     else:
#         turn_char ='X'
#         print('Ходят крестики')
#     row = int(input('Введите номер строки (1, 2, 3)')) - 1
#     column = int(input('Введите номер столбца (1, 2, 3)')) - 1
#     if area[row][column] == '*':
#         area[row][column] = turn_char
#     else:
#         print('Ячейка уже занята! Вы пропускаете ход!')
#         continue
#         draw_area()
#
#     draw_area()
# def check_win():
#     if area[0][0] == 'X' and area[0][1] and area[0][2]:

maps = [1,2,3,
        4,5,6,
        7,8,9]
win = [[0,1,2],
       [3,4,5],
       [6,7,8],
       [0,3,6],
       [1,4,7],
       [2,5,8],
       [0,4,8],
       [2,4,6]]
def print_maps():
    print(maps[0], end='')
    print(maps[1], end='')
    print(maps[2])

    print(maps[3], end='')
    print(maps[4], end='')
    print(maps[5])

    print(maps[6], end='')
    print(maps[7], end='')
    print(maps[8])

def step_maps(step,simbol):
    ind = maps.index(step)
    maps[ind] = simbol

def get_result():
    winner =''

    for i in win:
        if maps[i[0]] == 'X' and maps[i[1]] == 'X' and maps[i[2]] == 'X':
            winner ='X'
        if maps[i[0]] == 'O' and maps[i[1]] == 'O' and maps[i[2]] == 'O':
            winner = 'O'
    return winner




