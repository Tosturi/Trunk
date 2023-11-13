from import_matrix import maze_list

my_maze: list = maze_list()
new_maze: list = []

def step_down(maze, x=1, y=1):
    left = maze[y][x - 1]
    right = maze[y][x + 1]
    up = maze[y - 1][x]
    down = maze[y + 1][x]
    count = 0



def check_step(x, y, maze):
    left = maze[y][x-1]
    right = maze[y][x+1]
    up = maze[y-1][x]
    down = maze[y+1][x]
    if down == 0:
        return True
    elif up == 0:
        return True
    elif left == 0:
        return True
    elif right == 0:
        return True
    else:
        return False


for i in step_down(my_maze):
    for j in i:
        print(j, end=' ')
    print()
