// https://leetcode.com/problems/unique-morse-code-words/
class Solution {
    fun uniqueMorseRepresentations(words: Array<String>): Int {
        val alpha =
                arrayOf(
                        ".-",
                        "-...",
                        "-.-.",
                        "-..",
                        ".",
                        "..-.",
                        "--.",
                        "....",
                        "..",
                        ".---",
                        "-.-",
                        ".-..",
                        "--",
                        "-.",
                        "---",
                        ".--.",
                        "--.-",
                        ".-.",
                        "...",
                        "-",
                        "..-",
                        "...-",
                        ".--",
                        "-..-",
                        "-.--",
                        "--.."
                )
        val result =
                words
                        .map {
                            // leet code 코틀린 버젼 1.3 임..ㅠㅠ
                            // val converted = it.map { it.code - 'a'.code }.map { alpha[it] }
                            val converted = it.map { it.toInt() - 'a'.toInt() }.map { alpha[it] }
                            converted.joinToString(separator = "")
                        }
                        .toSet()
                        .size
        return result
    }
}

// // others
// 바로 정의 했음. array distinct 메소드를 사용했음!
// 별도 Set 으로 변경할 필요 없었음..
// class Solution {
//     val abc = arrayOf(".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..",
//
// "--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..")
//     fun uniqueMorseRepresentations(words: Array<String>): Int =
//         words.map { w -> w.map { abc[(it - 'a').toInt()] }.joinToString("") }.distinct().size
// }
