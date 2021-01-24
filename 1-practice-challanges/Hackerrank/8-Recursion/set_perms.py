result = dict()
result[1] = 1
result[2] = 2
result[3] = 4


def stepPerms(n):
    if n == 0:
        return 0
    if n in result.keys():
        return result[n]
    result[n] = stepPerms(n - 1) + stepPerms(n - 2) + stepPerms(n - 3)
    return result[n]
