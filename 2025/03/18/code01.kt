// https://leetcode.com/problems/divide-array-into-equal-pairs
class Solution {
    fun divideArray(nums: IntArray): Boolean {
        val numToCount = mutableMapOf<Int, Int>()

        for (num in nums) {
            numToCount[num] = numToCount.getOrDefault(num, 0) + 1
        }

        return numToCount.all { (_, count) -> count % 2 == 0 }
    }
}

class Solution {
    fun divideArray(nums: IntArray): Boolean {
        return nums.asList().groupBy { it }.all { (_, group) -> group.size % 2 == 0 }
    }
}