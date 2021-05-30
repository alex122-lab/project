a = [[9, 7, 5], [3, 1, 8]]
b = [[7, 6, 0], [1, 9, 3]]


class Matrix:

    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return ' '.join(map(str, self.lists))

    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + other.lists[i][j])
        return ' '.join(map(str, c))




matrix1 = Matrix(a)
matrix2 = Matrix(b)

print(matrix1)
print(matrix2)
print('-' * 30)
print(matrix1 + matrix2)

