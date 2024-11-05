# def draw_box():
#     for i in range(5):
#         print('!'*7)
#
# draw_box()
# print()
# draw_box()
from random import random


# def print_name(name):
#     print(name)
#
# print_name('Oleg')
# print_name('Sergey')

import random
def lottery(*args,**kwargs):
    tickets = [1, 2, 3 ,4, 5 , 6 , 7 , 8, 9, 10]
    win1 = random.choice(tickets)
    tickets.remove(win1)
    win2 = random.choice(tickets)
    print(*args)
    return win1, win2

win1, win2 = lottery('mon', 'tue')
print(win1, win2)

