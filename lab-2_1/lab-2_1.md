# Сам код решение, вывод ниже кода

```python
from pycryptosat import Solver
import itertools

s = Solver()
cnf = []


def vind(symbol, i, j):
    ind = (i - 1) * 3 + j
    if symbol == 'O':
        ind += 9
    return ind


def add_clause(vlist):
    l = []
    for symbol, i, j, sign in vlist:
        if sign == '+':
            l.append(vind(symbol, i, j))
        else:
            l.append(-vind(symbol, i, j))
    s.add_clause(l)
    cnf.append(l)


def print_cnf(filename):
    with open(filename, 'w') as fout:
        print('p cnf', 18, len(cnf), file=fout)
        for clause in cnf:
            print(" ".join(list(map(str, clause)) + ['0']), file=fout)


inds = range(1, 4)
field = [['.' for _ in range(4)] for _ in range(4)]

field[1][1] = 'X'
field[1][3] = 'O'
field[2][1] = 'O'
field[3][3] = 'X'

print("Исходное поле:")
for i in inds:
    for j in inds:
        print(field[i][j], end='')
    print()
print()

for i in inds:
    for j in inds:
        add_clause([('X', i, j, '-'), ('O', i, j, '-')])

for i in inds:
    for j in inds:
        if field[i][j] == 'X':
            add_clause([('X', i, j, '+')])
        elif field[i][j] == 'O':
            add_clause([('O', i, j, '+')])

free_cells = [(i, j) for i in inds for j in inds if field[i][j] == '.']

if free_cells:
    add_clause([('X', i, j, '+') for i, j in free_cells])

for idx1, (i1, j1) in enumerate(free_cells):
    for idx2, (i2, j2) in enumerate(free_cells):
        if idx1 < idx2:
            add_clause([('X', i1, j1, '-'), ('X', i2, j2, '-')])

win_combinations = [
    [(1, 1), (1, 2), (1, 3)], [(2, 1), (2, 2), (2, 3)], [(3, 1), (3, 2), (3, 3)],
    [(1, 1), (2, 1), (3, 1)], [(1, 2), (2, 2), (3, 2)], [(1, 3), (2, 3), (3, 3)],
    [(1, 1), (2, 2), (3, 3)], [(1, 3), (2, 2), (3, 1)]
]

for combo in win_combinations:
    add_clause([('X', i, j, '+') for i, j in combo])

print_cnf("cnf.txt")

sat, solution = s.solve()

if not sat:
    print('Нет решения')
else:
    new_field = [['.' for _ in range(4)] for _ in range(4)]
    for i in inds:
        for j in inds:
            new_field[i][j] = field[i][j]

    for i in inds:
        for j in inds:
            if field[i][j] == '.' and solution[vind('X', i, j)]:
                new_field[i][j] = 'X'

    print("Решение:")
    for i in inds:
        for j in inds:
            print(new_field[i][j], end='')
        print()


    def check_win(board):
        for combo in win_combinations:
            if all(board[i][j] == 'X' for i, j in combo):
                return True
        return False


    if check_win(new_field):
        print("X выиграл!")
    else:
        print("Ничья или игра продолжается")


def visualize_n_queens():
    N = int(input().strip())
    numbers = list(map(int, input().strip().split()))

    board = [['.' for _ in range(N)] for _ in range(N)]

    for num in numbers:
        if num > 0:
            pos = num - 1
            row = pos // N
            col = pos % N
            board[row][col] = 'Q'

    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()


if __name__ == "__main__":
    visualize_n_queens()
```

# Вывод:
```
Исходное поле:
X.O
O..
..X

Решение:
X.O
OX.
..X
X выиграл!
