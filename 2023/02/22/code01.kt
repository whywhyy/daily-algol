// https://leetcode.com/problems/single-element-in-a-sorted-array/
class Solution {
    fun singleNonDuplicate(nums: IntArray): Int {
        if (nums.size == 1) {
            return nums[0]
        }
        return nums.filterIndexed { idx, it ->
            if (idx != 0 && idx != nums.size - 1) {
                !(it == nums[idx - 1] || it == nums[idx + 1])
            } else if (idx == 0) {
                !(it == nums[idx + 1])
            } else {
                !(it == nums[idx - 1])
            }
        }[0]
    }
}
