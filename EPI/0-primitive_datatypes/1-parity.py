def get_bit(num):
    res = 0
    while num:
        res ^= num & 1
        num >>= 1
    return res

print(get_bit(20))