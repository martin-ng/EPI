def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits


print(count_bits(10))
'''
256 128 64 32 16 8 4 2 1 0
 0   0   0  0  0 1 0 1 0 0
'''
print(count_bits(15))
'''
256 128 64 32 16 8 4 2 1 0
 0   0   0  0  0 1 1 1 1
'''
