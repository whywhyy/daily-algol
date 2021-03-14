// Swapping Nodes in a Linked List
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

function swapNodes(head: ListNode | null, k: number): ListNode | null {
  const arr = [];
  
  let node = head;
  while(node){
    arr.push(node);
    node = node.next;
  }
  
  // node swap
  // [arr[k-1], arr[arr.length-k]] = [arr[arr.length-k], arr[k-1]];
  // [arr[k-1].next, arr[arr.length-k].next] = [arr[arr.length-k].next, arr[k-1].next];
  // if(k-2 >= 0 ){
  //   arr[k-2].next = arr[k-1];
  // }
  // if(arr.length-k-1 >= 0){
  //   arr[arr.length-k-1].next = arr[arr.length-k];
  // }

  // value swap
  [arr[k-1].val, arr[arr.length-k].val] = [arr[arr.length-k].val, arr[k-1].val];

  return arr[0];
};


// good
function swapNodes(head: ListNode | null, k: number): ListNode | null {
  let start = head;
  while(k>1) {
      k--;
      start = start.next;
  }
  let slow = head;
  let fast = start;
  while(fast.next !== null) {
      fast=fast.next;
      slow=slow.next;
  }
  let t = slow.val;
  slow.val = start.val;
  start.val = t;
  return head;
};


// good
function swapNodes(head: ListNode | null, k: number): ListNode | null {
  let frontNode = null;
  let endNode = null;
  let currentNode = head;
  let length = 0;
  
  while(currentNode) {
      length++;
      
      if(endNode) endNode = endNode.next;
      
      if(length === k) {
          frontNode = currentNode;
          endNode = head;
      }
      
      currentNode = currentNode.next;
  }
  
  let temp = frontNode.val;
  frontNode.val = endNode.val;
  endNode.val = temp;
  return head;
};