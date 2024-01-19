with open('maze-1.csv') as read_maze:
    one_row = read_maze.readlines()
    new_maze: list = []
    for li in one_row:
        new_maze.append(list(map(int, li.split(';'))))
t = 0


def pathfinder(maze, y=1, x=1):
    if y == len(maze)-2 and x == len(maze[0])-2:
        maze[y][x] = 'x'
        return maze, True
    else:
        for i in range(1, -2, -2):
            if maze[y][x] == 0:
                maze[y][x] = 2
            if maze[y+i][x] == 0:
                maze, flags = pathfinder(maze, y+i, x)
                if flags:
                    return maze, True
            if maze[y][x+i] == 0:
                maze, flags = pathfinder(maze, y, x+i)
                if flags:
                    return maze, True

        maze[y][x] = '#'
        return maze, False


LAB, flag = pathfinder(new_maze)

for k in LAB:
    for w in k:
        print(w, end=' ')
    print()
print(t)