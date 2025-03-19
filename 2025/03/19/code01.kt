class Solution {
    fun minOperations(nums: IntArray): Int {
        var result = 0
        nums.toList()
        for (i in 0 until nums.size - 2) {
            val current = nums[i]
            if (current == 0) {
                result += 1
                nums[i] = 1
                nums[i + 1] = nums[i + 1] xor 1
                nums[i + 2] = nums[i + 2] xor 1
            }
        }

        return if (nums.last() == 0 || nums.get(nums.size - 2) == 0 || nums.get(nums.size - 3) == 0)
                -1
        else result
    }
}
