class Cell:
    def __init__(self, param):
        self.param = param

    def __add__(self, other):
        return self.param + other.param

    def __sub__(self, other):
        return self.param - other.param if (self.param - other.param) > 0 else 'разность меньше 0'

    def __mul__(self, other):
        return self.param * other.param

    def __truediv__(self, other):
        return self.param // other.param


    def make_order(rows, nums):
        return  '\n'.join(['*' * rows for _ in range(nums // rows)]) + '\n' + '*' * (nums % rows)

cell_1 = Cell(30)
cell_2 = Cell(8)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)


print(Cell.make_order(6, 20))
