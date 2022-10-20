# A = {2, 3, 5, 7, 1}
# B = {2, 6, 7, 5, 3, 4}
# U = {1, 2, 3, 4, 5, 6, 7, 8}
A = [0] * 5
for i in range(5):
    print("Введіть " + str(i + 1) + "-й елемент першої множини")
    A[i] = int(input())
A.sort()
B = [0] * 6
for i in range(6):
    print("Введіть " + str(i + 1) + "-й елемент другої множини")
    B[i] = int(input())
B.sort()
print("A = " + str(A))
print("B = " + str(B))
U = [0] * 8
U = [1, 2, 3, 4, 5, 6, 7, 8]
U.sort()
print("U = " + str(U))


def task1():
    print("Об'єднання множин: " + str(add(A, B)))
    print("Перетин множин:", intersiction(A, B))
    print("Різниця множин B and A:", difference(A, B))
    print("Різниця множин A and B:", difference1(A, B))
    print("Доповнення: " + str(prutal(A, U)))
    print("Симетрична різниця: " + str(symmetricalDifference(A, B)))
    print("Декартовий добуток: ", str(decart(A, B)))
    subset()
    print("Перевірка на рівність множин: ", check(A,B))
    print("Переведена множини А в бітові рядки: ", transfer(A, U))
    print("Переведена множини B в бітові рядки: ", transfer1(B, U))
    print("Обєднання множин: ", associationBits(transfer(A, U), transfer1(B, U)))
    print("Перетин множин: ", intersectionBits(transfer(A, U), transfer1(B, U)))
    print("Різниця A and B", differenceBits(transfer(A, U), transfer1(B, U)))
    print("Симетрична різниця: ", symmetricDifferenceBits(transfer(A, U), transfer1(B, U)))


# union of two sets
def add(A, B):
    c = []
    for i in B:
        c.append(i)
    for j in A:
        c.append(j)
    return c


# elements of the set that are in three sets

def intersiction(A, B):
    a = []

    for b in A:
        if b in B:
            a.append(b)

    return a


def difference(A, B):
    a = []

    for b in B:
        if b not in A:
            a.append(b)

    return a


def difference1(A, B):
    a = []

    for b in A:
        if b not in B:
            a.append(b)
    return a


# plural complement


def prutal(A, U):
    a = []

    for c in U:
        if c not in A:
            a.append(c)
    return a


def symmetricalDifference(A, B):
    result = []
    for i in A:
        if not i in B:
            result.append(i)

    for i in B:
        if not i in A:
            result.append(i)

    return result


def decart(A, B):
    return [(a, b) for a in A for b in B]


def subset():
    if set(A) <= set(B):
        print("Множина A є підмножиною B")
    else:
        print("Множина A не є підмножиною B")


def check(A, B):
    for i in A:
        if i not in B:
            return False

    return True


def transfer(A, U):
    res = ""
    for u in U:
        if u in A:
            res += "1"
        else:
            res += "0"
    return res


def transfer1(B, U):
    res = ""
    for u in U:
        if u in B:
            res += "1"
        else:
            res += "0"
    return res


def associationBits(bita, bitb):
    arr = []
    for i in range(8):
        val = str(int(bita[i]) | int(bitb[i]))
        if val == "1":
            arr.append(i + 1)
    return arr


def intersectionBits(bita, bitb):
    arr = []
    for i in range(8):
        val = str(int(bita[i]) & int(bitb[i]))
        if val == "1":
            arr.append(i + 1);
    return arr


def differenceBits(bita, bitb):
    arr = []
    for i in range(8):
        val = str(int(bita[i]) & ~int(bitb[i]))
        if val == "1":
            arr.append(i + 1)
    return arr


def symmetricDifferenceBits(bita, bitb):
    arr = []
    for i in range(8):
        val = str(~int(bita[i]) & int(bitb[i]) | int(bita[i]) & ~int(bitb[i]))
        if val == "1":
            arr.append(i + 1);
    return arr


task1()
