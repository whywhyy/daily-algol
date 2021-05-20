//https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/600/week-3-may-15th-may-21st/3749/

/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function levelOrder(root: TreeNode | null): number[][] {
  const result = [];
  if (!root) {
    return [];
  }
  const queue = [root];
  while (queue.length) {
    const inputArr = [];
    const n = queue.length;
    for (let i = 0; i < n; i++) {
      const now = queue.shift();
      inputArr.push(now.val);
      if (now.left) {
        queue.push(now.left);
      }
      if (now.right) {
        queue.push(now.right);
      }
    }
    result.push(inputArr);
  }
  return result;
}

// refactor
function levelOrder(root: TreeNode | null): number[][] {
  const result = [];
  if (!root) {
    return [];
  }
  let queue = [root];
  while (queue.length) {
    const inputArr = [];
    const nowQ = queue.slice();
    queue.splice(0, queue.length);
    nowQ.map((node) => {
      inputArr.push(node.val);
      if (node.left) {
        queue.push(node.left);
      }
      if (node.right) {
        queue.push(node.right);
      }
    });
    result.push(inputArr);
  }
  return result;
}
