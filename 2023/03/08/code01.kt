/**
 * 최소값이 array 의 가장 작은값이 될줄알았지만, h가 매우 크다면 1이 될수도 있음
 *
 * 어떠한 정답값이 범위인데 이를 seach 하는 로직에 대해 잘 고민해야할듯함.
 *
 * 아래의 경우 최소한의 left를 찾아야 하는경우임
 *
 * 큰 경우 무조건 left = mid + 1 를 해서 search 하는 전략을 사용하였음.
 */
class Solution {
    fun minEatingSpeed(piles: IntArray, h: Int): Int {
        var left = 1
        var right = piles[0]
        piles.forEach { right = Math.max(right, it) }

        while (left < right) {
            var mid = left + (right - left) / 2
            var result = 0
            piles.forEach {
                if (it < mid) {
                    result += 1
                } else {
                    if (it % mid == 0) {
                        result += it / mid
                    } else {
                        result += it / mid + 1
                    }
                }
            }
            if (result > h) {
                left = mid + 1
            } else {
                right = mid
            }
        }

        return left
    }
}
