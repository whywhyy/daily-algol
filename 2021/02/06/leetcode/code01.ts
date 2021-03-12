// Binary Tree Right Side View
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

function rightSideView(root: TreeNode | null): number[] {
    if (root === null){
        return []
    }
    const queue = [];
    const result = [];
    queue.push({node:root, h:0, x:0}); // height , x 
    while (queue.length){
        // console.log(queue, result);
        const { node, h, x } = queue.shift();
        if(result.length < h+1){
            result.push( {node: node.val, x: x} );
        }else{
            const obj  = result.pop();
            result.push({ node : node.val, x: x});
        }
        if(node.left !== null){
            queue.push({node:node.left, h: h+1, x: x-1 })
        }
        
        if(node.right !== null){
            queue.push({node:node.right, h: h+1, x: x+1 })
        }
    }  

    return result.map(v => v.node)
};

// while 에서 queue.length 를 할것
function rightSideView(root: TreeNode | null): number[] {
    if(root === null || typeof root !== 'object') return [];
    let queue = [root];
    let result = [];
    
    while(queue.length) {
        let len = queue.length;
        result.push(queue[len - 1].val);
        for(let i = 0; i < len; ++i) {       
            let node = queue.shift();
            node.left && queue.push(node.left);
            node.right && queue.push(node.right);      
        }
    }

    return result;
    
};

function rightSideView(root: TreeNode | null): number[] {
    if (!root) {
        return []
    }
    
    const result = []
    let queue = [root]
    while (queue.length) {
        const nextLevel = queue
        result.push(nextLevel[nextLevel.length - 1].val)
        queue = []
        for (const n of nextLevel) {
            if (n.left) {
                queue.push(n.left)    
            }
            if (n.right) {
                queue.push(n.right)
            }
        }
    }
    
    return result    
};

function rightSideView( root: TreeNode | null ): number[] {
    if ( root === null ) {
      return [];
    }
  
    const result = [];
    let nodes = [ root ];
  
    while ( nodes.length > 0 ) {
      const temp = [];
  
      for ( let i = 0; i < nodes.length; i++ ) {
        const { left, right }: TreeNode = nodes[ i ];
  
        if ( left ) {
          temp.push( left );
        }
        if ( right ) {
          temp.push( right );
        }
      }
  
      result.push( nodes[ nodes.length - 1 ].val );
  
      nodes = temp;
    }
  
    return result;
  }