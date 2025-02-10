// https://leetcode.com/problems/clear-digits/description/?envType=daily-question&envId=2025-02-10

// my solution
import kotlin.collections.mutableListOf
class Solution {
    fun clearDigits(s: String): String {
        val stack = mutableListOf<String>()
        s.forEach {
            if (it.isDigit()) {
                stack.removeLast()
            } else {
                stack.add(it.toString())
            }
         }
         return stack.joinToString("") // 17ms
    }
}

// stack 2
class Solution {
    fun clearDigits(s: String): String {
        val stack = s.toCharArray()
        var size = 0
        s.forEach {
            if (it.isDigit()) {
                size -= 1
            } else {
                stack[size] = it
                size += 1
            }
         }
         // return stack.sliceArray(0 until size).joinToString("") // 객체 생성으로 40ms 
         return String(stack, 0 , size) // 객체 재사용으로 2ms 
    }
}

// two pointer
class Solution {
    fun clearDigits(s: String): String {
        var startPointer = 0
        val res = s.toCharArray()
        res.forEach {
            if (it.isDigit()) {
                startPointer--
            } else {
                if (startPointer >= 0 ) {
                    res[startPointer] = it
                }
                startPointer++
            }
        }
        return res.sliceArray(0 until startPointer).joinToString("")
    }
}