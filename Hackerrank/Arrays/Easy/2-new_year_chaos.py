
def new_year_chaos(self, q):
    counter = 0
    for i in range(len(q) - 1, 0, -1):
        if q[i] != i + 1:
            counter += 1
            q[i], q[i + 1] = q[i + 1], q[i]
        elif q[i - 2] == i + 1:
            counter += 2
            q[i - 2], q[i - 1] = q[i - 1], q[i - 2]
            q[i], q[i - 2] = q[i - 2], q[i]
        else:
            print("Too strong")
            return
    return counter
