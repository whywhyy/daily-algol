// https://leetcode.com/problems/power-of-four/
class Solution {
    fun isPowerOfFour(n: Int): Boolean {
        if (n < 1) {
            return false
        }
        var target = n
        while (target % 4 == 0) {
            target /= 4
        }
        return if (target != 1) {
            return false
        } else {
            return true
        }
    }
}

// bit 연산..!!!?
// https://leetcode.com/problems/power-of-four/discuss/1923369/Kotlin-oror-Beats-97-solution-oror-Bit-manipulation
class Solution {
    fun isPowerOfFour(n: Int): Boolean {
        var temp = n
        var c = 0
        if (n == 1) return true
        if (n == 0) return false
        while (temp.and(1) == 0) {
            c++
            temp = temp.shr(1)
        }
        return n >= 4 && n.and(n - 1) == 0 && c > 1 && c % 2 == 0
    }
}

class Solution {
    fun isPowerOfFour(n: Int): Boolean {
        return n > 0 && n.and(n - 1) == 0 && n % 3 == 1
    }
}
