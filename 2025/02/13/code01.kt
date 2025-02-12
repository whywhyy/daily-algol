

import kotlin.collections.mutableMapOf
import kotlin.comparisons.maxOf

class Solution { // 138 ms
    fun maximumSum(nums: IntArray): Int {
        val sumOfDigitsToMaxAndMaxTwoSum = mutableMapOf<Int, Pair<Int, Int>>()
        nums.forEach { 
            val sumOfDigits = it.toString().map { it.toString().toInt() }.sum()
            val maxAndTwoSum = sumOfDigitsToMaxAndMaxTwoSum.get(sumOfDigits)
            if (maxAndTwoSum == null) {
                sumOfDigitsToMaxAndMaxTwoSum.set(sumOfDigits, Pair(it, -1))
            } else {
                val (max, maxTwoSum) = maxAndTwoSum
                val currentTwoSum = maxOf(it + max, maxTwoSum)
                val currentMax = maxOf(it, max)
                sumOfDigitsToMaxAndMaxTwoSum.set(sumOfDigits, Pair(currentMax, currentTwoSum))
            }
        }
        
        return sumOfDigitsToMaxAndMaxTwoSum.maxOf {
                val (_, twoSum) = it.value
                twoSum
        }
    }
}

class Solution { // 120 ms
    fun maximumSum(nums: IntArray): Int {
        val sumOfDigitsToMaxAndMaxTwoSum = mutableMapOf<Int, Pair<Int, Int>>()
        var result = -1
        nums.forEach { 
            val sumOfDigits = it.toString().map { it.toString().toInt() }.sum()
            val maxAndTwoSum = sumOfDigitsToMaxAndMaxTwoSum.get(sumOfDigits)
            if (maxAndTwoSum == null) {
                sumOfDigitsToMaxAndMaxTwoSum.set(sumOfDigits, Pair(it, -1))
            } else {
                val (max, maxTwoSum) = maxAndTwoSum
                val currentTwoSum = maxOf(it + max, maxTwoSum)
                val currentMax = maxOf(it, max)
                sumOfDigitsToMaxAndMaxTwoSum.set(sumOfDigits, Pair(currentMax, currentTwoSum))
                
                result = maxOf(result, currentTwoSum)
            }
        }
        
        return result
    }
}


class Solution { // 122mx - 별다른 성능개선 없음
    fun maximumSum(nums: IntArray): Int {
        val sumOfDigitsToMaxValue = mutableMapOf<Int, Int>()
        var result = -1
        nums.forEach { 
            val sumOfDigits = it.toString().map { it.toString().toInt() }.sum()
            val maxValue = sumOfDigitsToMaxValue.get(sumOfDigits)
            if (maxValue == null) {
                sumOfDigitsToMaxValue.set(sumOfDigits, it)
            } else {
                val currentMax = maxOf(maxValue, it)
                sumOfDigitsToMaxValue.set(sumOfDigits, currentMax)
                
                result = maxOf(result, maxValue + it)
            }
        }
        
        return result
    }
}

class Solution { // 59 ms - converting sum to digit sum
    fun maximumSum(nums: IntArray): Int {
        val sumOfDigitsToMaxAndMaxTwoSum = mutableMapOf<Int, Pair<Int, Int>>()
        var result = -1
        nums.forEach { 
            val sumOfDigits = sumDigit(it)
            val maxAndTwoSum = sumOfDigitsToMaxAndMaxTwoSum.get(sumOfDigits)
            if (maxAndTwoSum == null) {
                sumOfDigitsToMaxAndMaxTwoSum.set(sumOfDigits, Pair(it, -1))
            } else {
                val (max, maxTwoSum) = maxAndTwoSum
                val currentTwoSum = maxOf(it + max, maxTwoSum)
                val currentMax = maxOf(it, max)
                sumOfDigitsToMaxAndMaxTwoSum.set(sumOfDigits, Pair(currentMax, currentTwoSum))
                
                result = maxOf(result, currentTwoSum)
            }
        }
        
        return result
    }

    fun sumDigit(value: Int): Int{
        var temp = value
        var result = 0
        while(temp > 0){
            result += temp % 10;
            temp /= 10;
        }
        return result
    }
}
