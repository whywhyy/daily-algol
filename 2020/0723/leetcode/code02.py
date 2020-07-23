# problem : Single Number III

from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result = []
        for a in Counter(nums).most_common():
            if a[1] == 1:
                result.append(a[0])

        return result

"""
# xor 연산이라니 
# 놀랍다. 
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        #there must be at least one digit diff for the two single int
        for num in nums:
            xor ^= num
        xor &= -xor #lowest digit value
        n1, n2 = 0, 0
        #divide to two groups, each one with one only int
        for num in nums:
            if xor & num:
                n1 ^= num
            else:
                n2 ^= num
        return [n1, n2]
"""



