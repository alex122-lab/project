class Stationery:
    def __init__(self, title='Синяя ручка'):
        self.title = title

    def drow(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def drow(self):
        print('Запуск отрисовки c ручкой')


class Pencil(Stationery):
    def drow(self):
        print('Запуск отрисовки c карандашом')


class Handle(Stationery):
    def drow(self):
        print('Подчёркиваем текст')

blue_pen = Stationery('Синяя Ручка')

stat = Stationery()
print(blue_pen.title)
stat.drow()
pen_1 = Pen('Красная ручка')
print(pen_1.title)
pen_1.drow()
pensil_1 = Pencil()
pensil_1.drow()
handle_1 = Handle()
handle_1.drow()

