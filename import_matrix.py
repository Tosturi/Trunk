def maze_list() -> list:
    """Создание матрицы лабиринта"""
    with open('maze-1.csv') as inputs:
        lin: list = inputs.readlines()
        old_matrix: list = []
        for i in lin:
            old_matrix.append(list(map(int, i.split(';'))))
        return old_matrix


if __name__ == '__main__':

    for i in maze_list():
        for j in i:
            print(j, end=' ')
        print()
