import collections
import random


# def find_E(nums, k):
#     d = collections.Counter(nums)
#
#     Eb = sum(nums) / 6
#     Eb_similar = 0
#     for val in d:
#         Eb_similar += val * ((d[val]**2) / 36)
#
#     res_E = Eb
#     n = 1
#     while n < k:
#         res_E += (Eb - Eb_similar)
#         n+=1
#
#     return res_E


def gener_pos():
    rand_nums = [random.randint(1, 1001) for _ in range(6)]
    rand_k = random.randint(1, 1001)
    return rand_nums, rand_k


import collections

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    k = int(input())
    d = collections.Counter(nums)

    Eb = sum(nums) / 6
    Eb_similar = 0
    for val in d:
        Eb_similar += val * ((d[val]**2) / 36)
    res_E = Eb
    n = 1
    while n < k:
        res_E += (Eb - Eb_similar)
        n+=1

    print(res_E)