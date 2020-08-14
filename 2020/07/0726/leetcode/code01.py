# Find Minimum in Rotated Sorted Array II

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums == None:
            return []
        nums = sorted(nums)
        return nums[0]

"""
# binary search 를 구현한 사람이 많다. 
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if(nums[0]<=nums[-1]):
            for num in nums:
                if(num<nums[0]):
                    return num
            return nums[0]
        def binarySearch(low, high):
            if(high-low == 1):
                print(low, high)
                return nums[high]
            mid = int((low+high)/2)
            if(nums[low]>nums[mid]):
                return binarySearch(low, mid)
            else:
                return binarySearch(mid, high)
            
        return binarySearch(0, len(nums)-1)
"""