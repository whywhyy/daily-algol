//  Trim a Binary Search Tree
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

function trimBST(root: TreeNode | null, low: number, high: number): TreeNode | null {
    let emptyNode = new TreeNode();
    emptyNode.left = root;
    emptyNode.right = root;
    let queue = [];
    queue.push({parent: emptyNode, direction:'left' ,node: root})
    while(queue.length){
        let {parent, direction, node} = queue.shift();
        if(node.val >= low && node.val <= high){
            if(node.left){
                queue.push({parent: node, direction:'left', node: node.left})    
            }
            if(node.right){
                queue.push({parent: node, direction:'right', node:node.right})
            }
        }
        else{
            if(node.val > high){
                node.right = null;
                if(node.left){
                    if(direction === 'left'){
                        parent.left = node.left
                        queue.push({parent: parent, direction:'left', node: node.left})
                    }else{
                        parent.right = node.left
                        queue.push({parent: parent, direction:'right', node: node.left})
                    }
                }else{
                    if(direction === 'left'){
                        parent.left = null;
                    }else{
                        parent.right =null;
                    }
                    node.left = null;
                }
            }else{
                node.left = null;
                if(node.right){
                    if(direction === 'left'){
                        parent.left = node.right
                        queue.push({parent: parent, direction:'left', node: node.right})
                    }else{
                        parent.right = node.right
                        queue.push({parent: parent, direction:'right', node: node.right})
                    }
                }else{
                    if(direction === 'left'){
                        parent.left = null;
                    }else{
                        parent.right =null;
                    }
                    node.right = null;
                } 
            }
        }
    }

    return emptyNode.left;
}

// GOOD
function trimBST(root: TreeNode | null, low: number, high: number): TreeNode | null {
    if (root === null) return null;
    
    if (root.val < low) {
        return trimBST(root.right, low, high);
    }
    if (root.val > high) {
        return trimBST(root.left, low, high);
    }
    
    root.left = trimBST(root.left, low, high);
    root.right = trimBST(root.right, low, high);
    return root;
    
};

function trimBST(root: TreeNode | null, low: number, high: number): TreeNode | null {
    if (root !== null) {
        if (root.val > high) return trimBST(root.left, low, high);
        if (root.val < low) return trimBST(root.right, low, high);

        root.left = trimBST(root.left, low, high);
        root.right = trimBST(root.right, low, high);
    }
    return root;       
};
