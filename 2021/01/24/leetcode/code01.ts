// Merge k Sorted Lists

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
    lists = lists.filter(node => node !== null)
    if(lists.length === 0){
        return null;
    }

    let result = new ListNode();
    let resultIdx = result;

    while(lists.length !== 0){

        let min_idx = 0;
        let min_v = lists[0].val;
        for(let i=0; i<lists.length;i++){
            if(lists[i].val <= min_v){
                min_v = lists[i].val;
                min_idx = i;
            }
        }
        
        resultIdx.val = min_v;

        lists[min_idx] = lists[min_idx].next; 
        if(lists[min_idx] === null){
            lists.splice(min_idx,1);
        }

        if(lists.length !== 0){
            resultIdx.next = new ListNode();
            resultIdx = resultIdx.next;
        }
    }

    return result;
};

// 2개씩 merge ! 1개 남을때 까지 !
function mergeKLists(lists: ListNode[]): ListNode | null {
    if (lists.length === 0) {
      return null;
    }
    while (lists.length > 1) {
      const a = lists.shift();
      const b = lists.shift();
      const h = merge(a, b);
      lists.push(h);
    }
    return lists[0];
  }
  
  function merge(a: ListNode | null, b: ListNode | null): ListNode | null {
    const dummy = new ListNode(0);
    let currentNode = dummy;
    while (a !== null && b !== null) {
      if (a.val < b.val) {
        currentNode.next = a;
        a = a.next;
      } else {
        currentNode.next = b;
        b = b.next;
      }
      currentNode = currentNode.next;
    }
    if (a !== null) {
      currentNode.next = a;
    }
    if (b !== null) {
      currentNode.next = b;
    }
    return dummy.next;
  }

//
  function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
    
    let merged = new ListNode(0);
    let ptr = merged;
    
    let arr = [];
    
    for (let list of lists) {
        while (list) {
            arr.push(list.val);
            list = list.next;
        }
    }
    
    arr.sort((a,b) => a-b);
    
    for (let num of arr) {
        ptr.next = new ListNode(num);
        ptr = ptr.next;
    }
    
    return merged.next;
    
};

// AWESOME 
function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
    if (lists.length === 0) {
        return null;
    }
    
    if (lists.length === 1) {
        return lists[0];
    }
    
    const next: Array<ListNode | null> = [];
    for (let i = 0; i < lists.length; i += 2) {
        next.push(merge2Lists(lists[i], lists[i + 1] || null));
    }
    return mergeKLists(next);
};

function merge2Lists(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    if (!l1) {
        return l2;
    }
    if (!l2) {
        return l1;
    }
    
    const prehead: ListNode | null = new ListNode();
    let current = prehead;
    while (l1 || l2) {
        if (!l2 || (l1 && l1.val <= l2.val)) {
            current.next = l1;
            l1 = l1.next;
        } else {
            current.next = l2;
            l2 = l2.next;
        } 
        current = current.next;
    }
    return prehead.next;
}