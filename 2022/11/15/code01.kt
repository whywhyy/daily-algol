/**
 * Example: var ti = TreeNode(5) var v = ti.`val` Definition for a binary tree node. class
 * TreeNode(var `val`: Int) {
 * ```
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * ```
 * }
 */
class Solution {
    fun countNodes(root: TreeNode?): Int {
        if (root == null) {
            return 0
        }
        var result = 0
        val queue = mutableListOf(root)
        while (queue.isNotEmpty()) {
            val currentNode = queue.removeAt(0)
            currentNode?.left?.let { queue.add(currentNode?.left) }
            currentNode?.right?.let { queue.add(currentNode?.right) }
            result += 1
        }

        return result
    }
}
