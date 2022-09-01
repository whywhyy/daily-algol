// https://leetcode.com/problems/count-good-nodes-in-binary-tree/

/**
 * Example: var ti = TreeNode(5) var v = ti.`val` Definition for a binary tree node. class
 * TreeNode(var `val`: Int) {
 * ```
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * ```
 * }
 */
// class TreeNode(var `val`: Int) {
//     var left: TreeNode? = null
//     var right: TreeNode? = null
// }

class Solution {
    fun goodNodes(root: TreeNode?): Int {
        val nowNode = root
        val queue = mutableListOf<Pair<TreeNode?, Int?>>(Pair(nowNode, null))
        var result = 0
        while (queue.isNotEmpty()) {
            val (currentNode, nowMax) = queue.removeAt(0)
            if (nowMax ?: currentNode!!.`val` <= currentNode!!.`val`) {
                result += 1
            }
            val nextMax = maxOf(nowMax ?: currentNode!!.`val`, currentNode!!.`val`)
            if (currentNode.left != null) {
                val nextLeft = currentNode.left
                queue.add(Pair(nextLeft, nextMax))
            }
            if (currentNode.right != null) {
                val nextRight = currentNode.right
                queue.add(Pair(nextRight, nextMax))
            }
        }
        return result
    }
}
