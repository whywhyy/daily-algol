// Vertical Order Traversal of a Binary Tree

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

function verticalTraversal(root: TreeNode | null): number[][] {
    let queue = [];
    let memoMap = new Map();
    queue.push({x:0, y:0, node:root});
    while(queue.length){
        let now = queue.shift();
        if(memoMap.has([now.x, now.y])){
            let insertArr = memoMap.get([now.x, now.y]);
            insertArr.push(now.node.val);
            memoMap.set([now.x, now.y], insertArr);
        }else{
            memoMap.set([now.x, now.y], [now.node.val]);
        }
        if(now.node.left){
            queue.push({x:now.x-1, y:now.y-1, node:now.node.left});
        }
        if(now.node.right){
            queue.push({x:now.x+1, y:now.y-1, node:now.node.right});
        }
    }
    // map => array => multiple sort
    let resultSorted = [...memoMap].sort((a,b) => (a[0][0]-b[0][0] || b[0][1]-a[0][1] || a[1]-b[1]));
    let result = [];
    console.log(resultSorted);

    // same X merge
    for(let i=0; i<resultSorted.length;i++){
        if(result.length === 0 ){
            result.push([resultSorted[i][0][0], resultSorted[i][1].sort((a,b)=> a-b)]);
        }else{
            if(result[result.length-1][0] === resultSorted[i][0][0]){
                resultSorted[i][1].sort((a,b)=> a-b).forEach((v) => {
                    result[result.length-1][1].push(v); 
                });
            }else{
                result.push([resultSorted[i][0][0], resultSorted[i][1].sort((a,b)=> a-b)]);
            }
        }   
    }
    
    // only v => v[1]
    result = result.map(v=>v[1]);
    return result;
};



interface ITraversalMap {
    [i:number]: Array<number[]>
    low:number
    high:number
}

function verticalTraversal(root: TreeNode | null): number[][] {
    const map = buildTraversalMap(root)
    
    let traversal:Array<number[]> = []
    for(let i=map.low;i<=map.high;++i){
        let item = []
        
        for(let j=0;j<map[i].length;++j){
            if(map[i][j]){
                map[i][j].sort((a,b)=>a-b)
                item = item.concat(map[i][j])
            }
        }
        
        traversal.push(item)
    }
    
    return traversal
}

function buildTraversalMap(root: TreeNode | null, i:number = 0, map: ITraversalMap = {low:0,high:0}, level: number = 0): ITraversalMap {
    if(!root)
        return map
    
    map[i] = map[i] || []
    map[i][level] = map[i][level] || []
    /*
    if(map[i][level][0] !== undefined && map[i][level][0] > root.val){
        map[i][level][1] = map[i][level][0]
        map[i][level][0] = root.val
    }else{
    */
        map[i][level].push(root.val)
    //}
    
    if(root.left){
        map.low = Math.min(map.low, i-1)
        buildTraversalMap(root.left, i-1, map, level+1)
    }
    if(root.right){
        map.high = Math.max(map.high, i+1)
        buildTraversalMap(root.right, i+1, map, level+1)
    }
    
    return map
};


//
class Triplet {
    public x: number;
    public y: number;
    public node: TreeNode;

    constructor(x: number, y: number, node: TreeNode) {
        this.x = x;
        this.y = y;
        this.node = node;
    }
}

function BFS(root: TreeNode) {
    const queue:Triplet[]  = [];
    const nodeArray: Triplet[] = [];
    queue.push(new Triplet(0, 0, root));
    while (queue.length > 0) {
        const element = queue.shift();
        nodeArray.push(element);
        if (element.node.left) {
            queue.push(new Triplet(element.x - 1, element.y + 1, element.node.left));
        }
        if (element.node.right) {
            queue.push(new Triplet(element.x + 1, element.y + 1, element.node.right));
        }
    }
    
    return nodeArray;
}

function verticalTraversal(root: TreeNode | null): number[][] {
    
    if (!root) {
        return null;
    }
    
    const nodeArray = BFS(root);
    const sortedArray = nodeArray.sort((a, b) => {
        if (a.x === b.x) {
            if (a.y === b.y) {
                return a.node.val - b.node.val;
            } else {
                return a.y - b.y;
            }
        } else {
            return a.x - b.x;
        }
    });
    // current array 를 만들어서 reuslt를 생성!
    const result = [];
    let currentX = sortedArray[0].x;
    let currentArray = [];
    for (const element of sortedArray) {
        if (element.x === currentX) {
            currentArray.push(element.node.val);
        } else {
            result.push(currentArray);
            currentX = element.x;
            currentArray = [];
            currentArray.push(element.node.val);
        }
    }
    
    result.push(currentArray);
    
    return result;
};

//
interface ITraversalMap {
    [i:number]: Array<number[]>
    low:number
    high:number
}

function verticalTraversal(root: TreeNode | null): number[][] {
    const map = buildTraversalMap(root)
    
    let traversal:Array<number[]> = []
    for(let i=map.low;i<=map.high;++i){
        let item = []
        
        for(let j=0;j<map[i].length;++j){
            if(map[i][j]){
                map[i][j].sort((a,b)=>a-b)
                item = item.concat(map[i][j])
            }
        }
        
        traversal.push(item)
    }
    
    return traversal
}

function buildTraversalMap(root: TreeNode | null, i:number = 0, map: ITraversalMap = {low:0,high:0}, level: number = 0): ITraversalMap {
    if(!root)
        return map
    
    map[i] = map[i] || []
    map[i][level] = map[i][level] || []
    /*
    if(map[i][level][0] !== undefined && map[i][level][0] > root.val){
        map[i][level][1] = map[i][level][0]
        map[i][level][0] = root.val
    }else{
    */
        map[i][level].push(root.val)
    //}
    
    if(root.left){
        map.low = Math.min(map.low, i-1)
        buildTraversalMap(root.left, i-1, map, level+1)
    }
    if(root.right){
        map.high = Math.max(map.high, i+1)
        buildTraversalMap(root.right, i+1, map, level+1)
    }
    
    return map
};


// 역시 GOOD
class NodeData {
    node: TreeNode | null;
    x: number;
    y: number;
}

function traversal(root: TreeNode | null, map: Map<number, NodeData[]>): void {

    let queue = new Array();
    queue.push({ node: root, x: 0, y: 0});
    
    while(queue.length != 0){
        const data = queue.shift();
        if(data.node){
            if(map.has(data.x)){
                const list = map.get(data.x);
                list.push(data);
                map.set(data.x, list);
            } else{
                map.set(data.x, [data]);
            }
            queue.push({ node: data.node.left, x: data.x - 1, y: data.y + 1});
            queue.push({ node: data.node.right, x: data.x + 1, y: data.y + 1});
        }
        
    }
}

function verticalTraversal(root: TreeNode | null): number[][] {
    let map = new Map();
    traversal(root, map);
    map = new Map([...map].sort((a, b) => a[0] - b[0]));
    let ans: number[][] = [];
    for (let value of map.values()) {
        value = value.sort((a,b) => {
            if(a.x==b.x){
                if(a.y == b.y){
                    return a.node.val - b.node.val;
                }
                return a.y-b.y;
            }
            return a.x-b.x;
        })
        ans.push(value.map((val) => {return val.node.val}));
    }
    return ans;
};
