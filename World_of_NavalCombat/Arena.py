

class Arena:
    """Работа с игровым полем"""
    def __init__(self, row=10, column=10):
        self.arena = [[(0, 0, False) for _ in range(row)] for _ in range(column)]

    def put_ship(self):
        pass

    def __set_cell(self, row, column):
        pass

    def __check_cell(self, row, column):
        pass


if __name__ == '__main__':
    field = Arena()

    for i in field.arena:
        for j in i:
            print(j, end='\t')
        print()
