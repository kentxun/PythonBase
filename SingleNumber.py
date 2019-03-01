

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    one = 0  # 出现一次的数
    two = 0  # 出现两次的数
    for i in nums:
        two |= (one & i)  # 要在更新one之前更新two
        one ^= i  # 更新one
        three = one & two  # one & two表示出现三次的数
        one &= ~three  # 抹去出现三次的数
        two &= ~three  # 抹去出现三次的数
    return one

out = singleNumber([1,1,3,2,3,3,1])
print(out)