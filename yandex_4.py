def check_basket(basket, n):
    set_basket = set(basket)

    for i in range(1, n+1):
        if i not in set_basket:
            return False
    return True


def find_price():
    param = [int(x) for x in input().split()]
    n = param[0]
    k = param[1]
    nums = [int(x) for x in input().split()]

    if n == k:
        return sum(nums)

    min_price = sum(nums)
    l, r = 0, 1

    while l < n-1 and r < n:
        if check_basket(nums[l:r], k) and r-l > k:
            min_price = min(min_price, sum(nums[l:r]))
            l+=1
        else:
            r+=1

    return min_price