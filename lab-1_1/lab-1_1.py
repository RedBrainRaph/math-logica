def print_truth_table_2var(tt, title):
    #Вывод таблицы истинности для функции от 2 переменных"""
    print(f"Функция: {title}")
    print("Таблица истинности:")
    print("+---+---+---------+")
    print("| A | B | f(A, B) |")
    print("+---+---+---------+")
    for A in [False, True]:
        for B in [False, True]:
            val = tt[(A, B)]
            print(f"| {int(A)} | {int(B)} |    {int(val)}    |")
    print("+---+---+---------+")
    print()


def print_equivalence_table_2var(f, g, title):
    #Вывод таблицы равносильности для двух функций от 2 переменных
    print(f"Равносильность: {title}")
    print("Таблица истинности:")
    print("+---+---+---------+---------+")
    print("| A | B | f(A, B) | g(A, B) |")
    print("+---+---+---------+---------+")
    for A in [False, True]:
        for B in [False, True]:
            f_val = f(A, B)
            g_val = g(A, B)
            print(f"| {int(A)} | {int(B)} |    {int(f_val)}    |    {int(g_val)}    |")
    print("+---+---+---------+---------+")
    print()


def print_equivalence_table_3var(f, g, title):
    # Вывод таблицы равносильности для двух функций от 3 переменных
    print(f"Равносильность: {title}")
    print("Таблица истинности:")
    print("+---+---+---+---------+---------+")
    print("| A | B | C | f(A,B,C)| g(A,B,C)|")
    print("+---+---+---+---------+---------+")
    for A in [False, True]:
        for B in [False, True]:
            for C in [False, True]:
                f_val = f(A, B, C)
                g_val = g(A, B, C)
                print(f"| {int(A)} | {int(B)} | {int(C)} |    {int(f_val)}    |    {int(g_val)}    |")
    print("+---+---+---+---------+---------+")
    print()


# Задание 1
# Конъюнкция (AND)
tt_and = {}
for A in [False, True]:
    for B in [False, True]:
        tt_and[(A, B)] = A and B
print_truth_table_2var(tt_and, "конъюнкция")

# Дизъюнкция (OR)
tt_or = {}
for A in [False, True]:
    for B in [False, True]:
        tt_or[(A, B)] = A or B
print_truth_table_2var(tt_or, "дизъюнкция")

# Импликация (A -> B)
tt_impl = {}
for A in [False, True]:
    for B in [False, True]:
        tt_impl[(A, B)] = (not A) or B
print_truth_table_2var(tt_impl, "импликация")

# Эквиваленция (A <-> B)
tt_eq = {}
for A in [False, True]:
    for B in [False, True]:
        tt_eq[(A, B)] = (A == B)
print_truth_table_2var(tt_eq, "эквиваленция")


# Задание 2
# 1. x → y = ¬x ∨ y
def f1(x, y):
    return (not x) or y

def g1(x, y):
    return (not x) or y

print_equivalence_table_2var(f1, g1, "x → y = ¬x ∨ y (формула замены импликации)")


# 2. x → y = ¬y → ¬x (закон контрапозиции)
def f2(x, y):
    return (not x) or y

def g2(x, y):
    return (not (not y)) or (not x)  # ¬y → ¬x = y ∨ ¬x

print_equivalence_table_2var(f2, g2, "x → y = ¬y → ¬x (закон контрапозиции)")


# 3. ¬(x & y) = ¬x ∨ ¬y (закон де Моргана)
def f3(x, y):
    return not (x and y)

def g3(x, y):
    return (not x) or (not y)

print_equivalence_table_2var(f3, g3, "¬(x & y) = ¬x ∨ ¬y (закон де Моргана)")


# 4. ¬(x ∨ y) = ¬x & ¬y (закон де Моргана)
def f4(x, y):
    return not (x or y)

def g4(x, y):
    return (not x) and (not y)

print_equivalence_table_2var(f4, g4, "¬(x ∨ y) = ¬x & ¬y (закон де Моргана)")


# 5. x & (y ∨ z) = (x & y) ∨ (x & z) (первый закон дистрибутивности)
def f5(x, y, z):
    return x and (y or z)

def g5(x, y, z):
    return (x and y) or (x and z)

print_equivalence_table_3var(f5, g5, "x & (y ∨ z) = (x & y) ∨ (x & z) (первый закон дистрибутивности)")


# 6. x ∨ (y & z) = (x ∨ y) & (x ∨ z) (второй закон дистрибутивности)
def f6(x, y, z):
    return x or (y and z)

def g6(x, y, z):
    return (x or y) and (x or z)

print_equivalence_table_3var(f6, g6, "x ∨ (y & z) = (x ∨ y) & (x ∨ z) (второй закон дистрибутивности)")


# 7. x ∨ (x & y) = x (закон поглощения)
def f7(x, y):
    return x or (x and y)

def g7(x, y):
    return x

print_equivalence_table_2var(f7, g7, "x ∨ (x & y) = x (закон поглощения)")


# 8. x & (x ∨ y) = x (закон поглощения)
def f8(x, y):
    return x and (x or y)

def g8(x, y):
    return x

print_equivalence_table_2var(f8, g8, "x & (x ∨ y) = x (закон поглощения)")


# 9. (x & y) ∨ (x & ¬y) = x (закон склеивания)
def f9(x, y):
    return (x and y) or (x and (not y))

def g9(x, y):
    return x

print_equivalence_table_2var(f9, g9, "(x & y) ∨ (x & ¬y) = x (закон склеивания)")


# 10. (x ∨ y) & (x ∨ ¬y) = x (закон склеивания)
def f10(x, y):
    return (x or y) and (x or (not y))

def g10(x, y):
    return x

print_equivalence_table_2var(f10, g10, "(x ∨ y) & (x ∨ ¬y) = x (закон склеивания)")


# 11. x ∨ (¬x & y) = x ∨ y (закон сокращения)
def f11(x, y):
    return x or ((not x) and y)

def g11(x, y):
    return x or y

print_equivalence_table_2var(f11, g11, "x ∨ (¬x & y) = x ∨ y (закон сокращения)")


# 12. x & (¬x ∨ y) = x & y (закон сокращения)
def f12(x, y):
    return x and ((not x) or y)

def g12(x, y):
    return x and y

print_equivalence_table_2var(f12, g12, "x & (¬x ∨ y) = x & y (закон сокращения)")
