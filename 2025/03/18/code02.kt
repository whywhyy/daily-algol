class Solution {
    fun longestNiceSubarray(nums: IntArray): Int {
        var result = 1

        for (i in 0 until nums.size) {
            val niceCandidates = mutableSetOf<Int>()
            niceCandidates.add(nums[i])
            for (j in i + 1 until nums.size) {
                val currentValue = nums[j]
                val allNice = niceCandidates.all { currentValue and it == 0 }
                if (allNice) {
                    niceCandidates.add(currentValue)
                    result = Math.max(result, niceCandidates.size)
                } else {
                    break
                }
            }
        }

        return result
    }
}

// with bitmask
class Solution {
    fun longestNiceSubarray(nums: IntArray): Int {
        var result = 1

        for (i in 0 until nums.size) {
            var currentResult = 1
            var currentValue = nums[i]
            for (j in i + 1 until nums.size) {
                if (currentValue and nums[j] == 0) {
                    currentValue = currentValue or nums[j]
                    currentResult += 1
                } else {
                    break
                }
                result = Math.max(result, currentResult)
            }
        }

        return result
    }
}

// sliding window - 5ms
class Solution {
    fun longestNiceSubarray(nums: IntArray): Int {
        var result = 1
        var startWindow = 0
        var currentBitMask = 0

        for (i in 0 until nums.size) {
            var endWindow = i
            val currentValue = nums[i]
            if (currentBitMask and currentValue == 0) {
                currentBitMask = currentBitMask or currentValue
            } else {
                while (startWindow < endWindow && currentBitMask and currentValue != 0) {
                    currentBitMask = currentBitMask xor nums[startWindow]
                    startWindow += 1
                }
            }
            currentBitMask = currentBitMask or currentValue
            result = Math.max(result, endWindow - startWindow + 1)
        }

        return result
    }
}
