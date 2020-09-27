# Largest Number
# 핰 이방법 '도' 맞네 ! max([0], [-1]) 를 아는것이 핵심 ! 
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        max_len = max([len(str(i)) for i in nums])
        str_nums = [[str(val), idx] for idx, val in enumerate(nums)]
        for i in range(len(str_nums)):
            str_nums[i][0] += max(str_nums[i][0][-1], str_nums[i][0][0]) * (max_len - len(str_nums[i][0]) )

        str_nums = sorted(str_nums, key = lambda x : -int(x[0]))
        result = []
        for i in str_nums:
            result.append(str(nums[i[1]]))
        
        return str(int("".join(result)))

# Largest Number
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums = sorted(nums,key=cmp_to_key(lambda x,y : 1 if int(x+y) < int(y+x) else -1 ))
        return str(int("".join(nums)))


# # 보통의 방법 비교용 클래스를 생성
# # def __lt__(x,y): return x+y > y+x 로 비교 sort 를 위해 생성 
# class LargerNumKey(str):
#     def __lt__(x, y):
#         return x+y > y+x
        # class Solution:
#     def largestNumber(self, nums):
#         largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
#         return '0' if largest_num[0] == '0' else largest_num


# 클래스 내부에 class 를 생성 ! 
# class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
#         class Comparator(str):
#             def __lt__(x, y):
#                 return x+y > y+x

#         a = "".join(sorted(map(str, nums), key=Comparator))
#         if a[0] == '0':
#             return "0"
#         else:
#             return a

# # 내가 풀려던 방법 !
# # 뒤에 max(ns[0], ns[-1]) * d 를 한다 !
# class Solution:
#     def largestNumber(self, nums) -> str:
#         max_l = len(str(max(nums)))
#         nums = list(map(lambda x: str(x), nums))
        
#         new_nums = []
#         for ns in nums:
#             d = max_l + len(ns)
#             new_nums.append(ns + max(ns[0], ns[-1])*d)
#         r = "".join([n[1] for n in sorted(zip(new_nums, nums), reverse=True)])
#         return "0" if int(r) == 0 else r
