// https://leetcode.com/problems/numbers-with-same-consecutive-differences/
class Solution {
    fun numsSameConsecDiff(n: Int, k: Int): IntArray {

        var results = (1..9).toMutableList()
        var nowN = 1
        while (nowN < n) {
            nowN += 1
            val currentSize = results.size
            for (i in 0..currentSize - 1) {
                var currentValue = results.removeAt(0)
                var nextLastValues = mutableListOf<Int>()

                var currentLastValue = currentValue % 10
                if (currentLastValue + k < 10) {
                    nextLastValues.add(currentLastValue + k)
                }
                if (currentLastValue - k >= 0) {
                    nextLastValues.add(currentLastValue - k)
                }
                for (nextLastValue in nextLastValues.toSet()) {
                    results.add(currentValue * 10 + nextLastValue)
                }
            }
        }
        return results.toIntArray()
    }
}

// repeat 사용
// queue foreach 동작, nextQueue 로 임시저장한후 동작
class Solution {
    fun numsSameConsecDiff(n: Int, k: Int): IntArray {
        val digits = (0..9)

        if (n == 1) return digits.map { it }.toIntArray()

        var queue = LinkedList<Int>().also { q -> digits.drop(1).forEach { q.add(it) } }

        repeat(n - 1) {
            val nextLevelQueue = LinkedList<Int>()

            queue.forEach { num ->
                val tailDigit = num % 10
                val nextDigits = mutableListOf(tailDigit + k)

                if (k > 0) nextDigits.add(tailDigit - k)

                nextDigits.filter { it in digits }.mapTo(nextLevelQueue) { num * 10 + it }
            }
            queue = nextLevelQueue
        }

        return queue.sorted().toIntArray()
    }
}
