// https://leetcode.com/problems/power-of-three/
class Solution {
    fun isPowerOfThree(n: Int): Boolean {
        var now = n
        while (now % 3 == 0 && now > 0) {
            now /= 3
        }
        now == 1
    }
}
