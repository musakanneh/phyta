import bisect

n, d = map(int, input().split())
exp = list(map(int, input().split()))
arr = sorted(exp[0:d])
mid = d // 2
count = 0

"""https://www.youtube.com/watch?v=60o-TJJ1kqg"""


def activity_notifications(arr, d, mid):
    if d % 2 == 0:
        return sum(arr[mid - 1: mid + 1]) / 2
    else:
        return arr[mid]


for i in range(d, n):
    if exp[i] >= 2 * activity_notifications(arr, d, mid):
        count += 1
    del arr[bisect.bisect_left(arr, exp[i - d])]
    bisect.insort(arr, exp[i])
print(count)
