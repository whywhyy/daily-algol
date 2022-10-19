// https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
/**
 * Example: var ti = TreeNode(5) var v = ti.`val` Definition for a binary tree node. class
 * TreeNode(var `val`: Int) {
 * ```
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * ```
 * }
 */
class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun verticalTraversal(root: TreeNode?): List<List<Int>> {

        var nodes = mutableListOf<TreeNode>()
        var queue = mutableListOf<TreeNode>()
        if (root != null) {
            queue.add(root)
        }
        while (queue.isNotEmpty()) {
            var currentNode = queue.removeAt(0)
            nodes.add(currentNode)
            if (currentNode.left != null) {
                queue.add(currentNode.left)
            }
            if (currentNode.right != null) {
                queue.add(currentNode.right)
            }
        }
        
        return listOf(listOf(1, 2))
    }
}
