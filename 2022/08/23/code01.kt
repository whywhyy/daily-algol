// https://leetcode.com/problems/palindrome-linked-list/
/**
 * Example: var li = ListNode(5) var v = li.`val` Definition for singly-linked list. class
 * ListNode(var `val`: Int) {
 * ```
 *     var next: ListNode? = null
 * ```
 * }
 */
class Solution {
    fun isPalindrome(head: ListNode?): Boolean {
        var stack = mutableListOf<Int>()
        var nowNode = head
        while (nowNode != null) {
            stack.add(nowNode.`val`)
            nowNode = nowNode.next
        }
        while (stack.size > 1 && stack.first() === stack.last()) {
            stack.removeAt(0)
            stack.removeAt(stack.size - 1)
        }

        return if (stack.size <= 1) {
            true
        } else {
            false
        }
    }
}
