from collections import deque
from img import *

def start():
    A = []
    B = [{}, {}]
    v = int(input("1.Доска 13*13 \n2.Доска 19*19\n"))
    if v == 1:
        A = board(13)
    if v == 2:
        A = board(19)
    output(A)
    # get_board_img(A)
    what_move = 0
    not_end = True
    scoreW = 0
    scoreB = 0
    while not_end:
        what_move += 1
        s = move(A, B, what_move)
        if what_move % 2 == 1:
            scoreB += s
        else:
            scoreW += s
        output(A)
        # get_board_img(A)
        if s != 0:
           print("Всего захвачено черных камней:", scoreW, "\nВсего захвачено белых камней", scoreB)

    print("Сыграть еще раз?")
    v = int(input("1.Да 2.Нет\n"))
    if v == 1:
        start()
    return

def move(A, B, what_move):
    x = y = 0
    black = "B"
    white = "W"
    whose_move_help = [["черных.", "белых."], [black, white]]
    whose_move = (what_move+1) % 2
    print("Ход", whose_move_help[0][whose_move], "Введите координаты вашего хода.")

    coor = True
    while coor:
        y = int(input("Координата по Х: ")) - 1
        x = len(A) - int(input("Координата по Y: "))
        if y >= len(A) or y < 0 or x >= len(A) or x < 0 or len(A[x][y]) != 2:
            print("Такой ход невозможен, введите другие координаты.")
        else:
            coor = False
    A[x][y] += whose_move_help[1][whose_move]
    B = arr_in_graph(A)

    # B[whose_move][(x, y)] = []
    # if x - 1 < len(A) and x - 1 >= 0 and len(A[x - 1][y]) == 3 and A[x - 1][y][2] == A[x][y][2]:
    #     B[whose_move][(x, y)].append((x - 1, y))                                                        # ЖОСКИЙ КОСТЫЛЬ
    #     B[whose_move][(x - 1, y)].append((x, y))
    # if x + 1 < len(A) and x + 1 >= 0 and len(A[x + 1][y]) == 3 and A[x + 1][y][2] == A[x][y][2]:
    #     B[whose_move][(x, y)].append((x + 1, y))
    #     B[whose_move][(x + 1, y)].append((x, y))
    # if y - 1 < len(A) and y - 1 >= 0 and len(A[x][y - 1]) == 3 and A[x][y - 1][2] == A[x][y][2]:
    #     B[whose_move][(x, y)].append((x, y - 1))
    #     B[whose_move][(x, y - 1)].append((x, y))
    # if y + 1 < len(A) and y + 1 >= 0 and len(A[x][y + 1]) == 3 and A[x][y + 1][2] == A[x][y][2]:
    #     B[whose_move][(x, y)].append((x, y + 1))
    #     B[whose_move][(x, y + 1)].append((x, y))

    s = regulations(A, B, whose_move)
    if s != 0:
       print("Захвачено", s, "камней")
    return s

def regulations(A, B, whose_move):
    s = 0
    n = len(A)
    moves = set()

    enemy_move = (whose_move + 1) % 2

    for elem in B[enemy_move]:
        moves.add(elem)
    for elem in B[whose_move]:
        moves.add(elem)

    C = graph_in_groups(B[enemy_move])                      # снимаются только противополодного цвета
    for arr in C:
        if len(groups_air(arr, n, moves)) == 0:
            s += len(arr)
            for kart in arr:
                A[kart[0]][kart[1]] = A[kart[0]][kart[1]][0:2]
    return s

def board(n = 13):
    A = []
    for i in range(n):
        A.append(['cc'] * n)

    A[0][0] = 'lu'
    A[0][n-1] = 'ru'
    A[n-1][0] = 'ld'
    A[n-1][n-1] = 'rd'

    for i in range(1, n-1):
        A[i][0] = 'lc'
        A[i][n-1] = 'rc'
        A[0][i] = 'ur'
        A[n-1][i] = 'dr'
    return A

def output(A):
    for row in A:
        for elem in row:
            if elem == 'cc':
                print('┼', end='')
            elif elem == 'lu':
                print('┌', end='')
            elif elem == 'ru':
                print('┐', end='')
            elif elem == 'ld':
                print('└', end='')
            elif elem == 'rd':
                print('┘', end='')
            elif elem == 'lc':
                print('├', end='')
            elif elem == 'rc':
                print('┤', end='')
            elif elem == 'ur':
                print('┬', end='')
            elif elem == 'dr':
                print('┴', end='')
            else:
                print(elem[2], end='')
        print()
    return

def arr_in_graph(A):

    def interval(i, n):
        if i >= 0 and i < n:
            return True
        return False

    graphBW = [{}, {}]
    for i in range(len(A)):
        for j in range(len(A[0])):
            if len(A[i][j]) == 3:
                if A[i][j][2] == 'B':
                    BW = 0
                else:
                    BW = 1
                graphBW[BW][(i, j)] = []
                if interval(i-1, len(A)) and len(A[i-1][j]) == 3 and A[i-1][j][2] == A[i][j][2]:
                    graphBW[BW][(i, j)].append((i-1, j))                                                #ЖОСКИЙ КОСТЫЛЬ
                if interval(i+1, len(A)) and len(A[i+1][j]) == 3 and A[i+1][j][2] == A[i][j][2]:
                    graphBW[BW][(i, j)].append((i+1, j))                                                #ОЧЕНЬ
                if interval(j-1, len(A)) and len(A[i][j-1]) == 3 and A[i][j-1][2] == A[i][j][2]:
                    graphBW[BW][(i, j)].append((i, j-1))
                if interval(j+1, len(A)) and len(A[i][j+1]) == 3 and A[i][j+1][2] == A[i][j][2]:
                    graphBW[BW][(i, j)].append((i, j+1))
    return graphBW

def graph_in_groups(G):
    C, queue, visited = [], deque([]), set()
    for root in G:
        if root not in visited:
            C.append([root])
            visited.add(root)
            queue = deque([root])
            while queue:
                elem = queue.popleft()
                for kart in G[elem]:
                    if kart not in visited:
                        C[len(C)-1].append(kart)
                        visited.add(kart)
                        queue.append(kart)
    return C

def groups_air(arr, n, moves):
    air = []
    for kart in arr:
        if kart[0] - 1 >= 0 and  kart[0] - 1 < n and (kart[0] - 1, kart[1]) not in moves and (kart[0] - 1, kart[1]) not in set(air):
            air.append((kart[0] - 1, kart[1]))
        if kart[0] + 1 >= 0 and  kart[0] + 1 < n and (kart[0] + 1, kart[1]) not in moves and (kart[0] + 1, kart[1]) not in set(air):
            air.append((kart[0] + 1, kart[1]))
        if kart[1] - 1 >= 0 and  kart[1] - 1 < n and (kart[0], kart[1] - 1) not in moves and (kart[0], kart[1] - 1) not in set(air):
            air.append((kart[0], kart[1] - 1 ))
        if kart[1] + 1 >= 0 and  kart[1] + 1 < n and (kart[0], kart[1] + 1) not in moves and (kart[0], kart[1] + 1) not in set(air):
            air.append((kart[0], kart[1] + 1))
    return air

#[['cc', 'lu', 'ru', 'ld', 'rd', 'lc', 'rc', 'ur', 'dr'],
# ['ccB', 'luB', 'ruB', 'ldB', 'rdB', 'lcB', 'rcB', 'urB', 'drB'],
# ['ccW', 'luW', 'ruW', 'ldW', 'rdW', 'lcW', 'rcW', 'urW', 'drW']]

start()
