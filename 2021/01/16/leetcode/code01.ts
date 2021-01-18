// Kth Largest Element in an Array

function findKthLargest(nums: number[], k: number): number {
    nums.sort((a,b)=>{return a-b});
    return nums[nums.length-k]
};