# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

print('Введите размер шоколадки n × m и сколько долек нужно отломить.')
n, m, k = int(input()), int(input()), int(input())
f = False
if k < m * n and (k >= n or k >= m):
    for i in range(1, n + 1):
        if i * m == k or (n - i) * m == k:
            f = True
            break
        else:
            for j in range(1, m + 1):
                if j * n == k or (m - j) * n == k:
                    f = True
                    break
if f:
    print('Можно разломить шоколадку на два прямоугольника.')
else:
    print('Разломить шоколадку не получится.')
