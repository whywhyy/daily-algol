/**
 * The API guess is defined in the parent class.
 * @param num your guess
 * @return -1 if num is higher than the picked number 1 if num is lower than the picked number
 * ```
 *               otherwise return 0
 * ```
 * fun guess(num:Int):Int {}
 */
class Solution : GuessGame() {
    override fun guessNumber(n: Int): Int {
        var currentMin: Long = 1
        var currentMax: Long = n.toLong()
        var gussed = (currentMin + currentMax).div(2)
        while (guess(gussed.toInt()) != 0) {
            // print(gussed)
            val currentGuess = guess(gussed.toInt())
            if (currentGuess == 1) {
                currentMin = gussed + 1
            }
            if (currentGuess == -1) {
                currentMax = gussed - 1
            }
            // overflow 생각해야함!!
            gussed = (currentMin + currentMax).div(2)
        }

        return gussed.toInt()
    }
}

// when 절 잘 사용한듯
// overflow 를 잘 피해감 - left 에서 center 까지의 거리만큼만 더하면됨
class Solution : GuessGame() {
    override fun guessNumber(n: Int): Int {
        var left = 1
        var right = n
        var center = (left + right) / 2
        while (left <= right) {
            center = (right - left) / 2 + left
            when (guess(center)) {
                0 -> {
                    return center
                }
                1 -> {
                    left = center + 1
                }
                -1 -> {
                    right = center - 1
                }
            }
        }
        return -1
    }
}
