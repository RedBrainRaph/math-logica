[Задание взято](https://github.com/lapkin25/comp-logic/blob/main/lab2/lab2.py)

# Код, ниже вывод
```python
# Заготовка для лабораторной работы 2

# возвращает таблицу истинности по кортежу значений функции 3 переменных
def truth_table_by_vec(v):
    assert(len(v) == 8)
    tt = {}
    i = 0
    for A in range(2):
        for B in range(2):
            for C in range(2):
                tt[A, B, C] = v[i]
                i += 1
    return tt

# возвращает таблицу истинности по заданной функции 3 переменных
def truth_table_by_func(f):
    tt = {}
    for A in range(2):
        for B in range(2):
            for C in range(2):
                tt[A, B, C] = f(A, B, C)
    return tt

def f_maj(x, y, z):
    return x and y or x and z or y and z

def f(x, y, z):
    return y | z & ~x

# принимает на вход таблицу истинности и выдает строку с СДНФ
def fdnf(tt):
    return ' | '.join(map(conj_str, [key for key in tt if tt[key]]))

# принимает на вход кортеж значений переменных и выдает элементарную конъюнкцию с такими степенями переменных
def conj_str(vars):
    var_names = ('x', 'y', 'z')
    return '&'.join(map(literal_str, var_names, vars))

# принимает на вход имя переменной (str) и ее степень (bool), возвращает литерал
def literal_str(name, deg):
    if deg:
        return name
    else:
        return '~' + name

# принимает на вход таблицу истинности и выдает строку с СКНФ
def fcnf(tt):
    # собираем дизъюнкты для строк, где функция равна 0
    disjuncts = []
    for key in tt:
        if not tt[key]:  # если значение функции равно 0
            # создаем дизъюнкт: для переменной, равной 0, берем саму переменную,
            # для переменной, равной 1, берем отрицание
            disjunct_parts = []
            for i, var_name in enumerate(('x', 'y', 'z')):
                if key[i] == 0:  # если переменная в наборе равна 0, берем её без отрицания
                    disjunct_parts.append(var_name)
                else:  # если переменная равна 1, берем её с отрицанием
                    disjunct_parts.append('~' + var_name)
            disjuncts.append('(' + '|'.join(disjunct_parts) + ')')
    return '&'.join(disjuncts)

# тестирование функции literal_str
print("Тест literal_str:")
print(literal_str('A', 1))
print(literal_str('B', 0))
print()

# тестирование функции conj_str
print("Тест conj_str:")
print(conj_str((0, 1, 0)))
print()

# создаем таблицу истинности для функции f
tt = truth_table_by_func(f)
print("Таблица истинности для функции f(x,y,z) = y | z & ~x:")
for key in sorted(tt.keys()):
    print(f"{key} -> {tt[key]}")
print()

# выводим СДНФ
print("СДНФ (совершенная дизъюнктивная нормальная форма):")
print(fdnf(tt))
print()

# выводим СКНФ
print("СКНФ (совершенная конъюнктивная нормальная форма):")
print(fcnf(tt))
print()

# демонстрация работы с функцией мажоритарности
print("=" * 50)
print("Демонстрация для функции мажоритарности:")
tt_maj = truth_table_by_func(f_maj)
print("СДНФ для f_maj:")
print(fdnf(tt_maj))
print("СКНФ для f_maj:")
print(fcnf(tt_maj))
```
# Вывод
```
Тест literal_str:
A
~B

Тест conj_str:
~x&y&~z

Таблица истинности для функции f(x,y,z) = y | z & ~x:
(0, 0, 0) -> 0
(0, 0, 1) -> 1
(0, 1, 0) -> 1
(0, 1, 1) -> 1
(1, 0, 0) -> 0
(1, 0, 1) -> 0
(1, 1, 0) -> 1
(1, 1, 1) -> 1

СДНФ (совершенная дизъюнктивная нормальная форма):
~x&~y&z | ~x&y&~z | ~x&y&z | x&y&~z | x&y&z

СКНФ (совершенная конъюнктивная нормальная форма):
(x|y|z)&(~x|y|z)&(~x|y|~z)

==================================================
Демонстрация для функции мажоритарности:
СДНФ для f_maj:
~x&y&z | x&~y&z | x&y&~z | x&y&z
СКНФ для f_maj:
(x|y|z)&(x|y|~z)&(x|~y|z)&(~x|y|z)
