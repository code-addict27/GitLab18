l = int(input())
ls = []
for i in range(l):
    ls.append(input())
ls.sort()


def commonprefix(a, b):
    ini_strlist = [a, b]
    res = ''
    prefix = ini_strlist[0]

    for string in ini_strlist[1:]:
        while string[:len(prefix)] != prefix and prefix:
            prefix = prefix[:len(prefix) - 1]
        if not prefix:
            break
    res = prefix
    return res


rs = 0
for i in range(l):
    for j in range(i + 1, l):
        rs += len(commonprefix(ls[i], ls[j])) ** 2

print(rs)
