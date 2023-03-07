import kotlin.math.sqrt

// 매번 n 까지 약수 찾는건 느림..
class Solution {
    fun minimumTime(time: IntArray, totalTrips: Int): Long {
        val valueToCount = mutableMapOf<Long, Long>()
        time.forEach {
            val currentCount = valueToCount.getOrDefault(it.toLong(), 0)
            valueToCount.set(it.toLong(), currentCount + 1)
        }

        var currentTotalTrips: Long = 0
        var result: Long = 0
        // min -
        while (true) {
            result += 1
            val allDvisors = getDvisor(result)
            allDvisors.forEach { currentTotalTrips += valueToCount.getOrDefault(it, 0.toLong()) }
            if (currentTotalTrips >= totalTrips.toLong()) {
                break
            }
        }
        return result
    }

    fun getDvisor(n: Long): List<Long> {
        val results = mutableListOf<Long>()
        for (i in 1..sqrt(n.toDouble()).toLong()) {
            if (n % i == 0.toLong()) {
                results.add(i)
                if (n / i != i) {
                    results.add(n / i)
                }
            }
        }
        return results
    }
}

/**
 * 가장 빨리 끝난경우 1, 가장 오래 걸리는경우 min(times)
 *
 * totalTrip binarySearch 를 이용하여 값을 찾아님
 * - binarySearch 1, max
 * - mid => left + (right - left) / 2
 * - mid 를 했을때, mid 의 결과가 더 크면 right를 줄임 => right = mid
 * - mid 를 했을때, mid 의 결과가 더 작음, left => mid + 1 해줌!
 */
class Solution {
    fun minimumTime(time: IntArray, totalTrips: Int): Long {
        var left: Long = 1
        var min = time[0]
        time.forEach { min = Math.min(min, it) }
        var right: Long = min.toLong() * totalTrips.toLong()
        while (left < right) {
            var mid: Long = (right - left) / 2 + left

            var total = totalTripInGivenTime(time, mid)
            if (total < totalTrips) {
                left = mid + 1
            } else {
                right = mid
            }
        }

        return left
    }

    fun totalTripInGivenTime(time: IntArray, givenTime: Long): Long {
        var totalTrips: Long = 0
        time.forEach { totalTrips += (givenTime / it.toLong()).toLong() }
        return totalTrips
    }
}
