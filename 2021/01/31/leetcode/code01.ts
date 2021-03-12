// Next Permutation

/**
 Do not return anything, modify nums in-place instead.
 */
function nextPermutation(nums: number[]): void {
    let isFinish = false;
    // to be change i
    for(let i=nums.length-2;i>=0;i--){
        if(isFinish === true){
            break
        }
        for(let j=nums.length-1; j>i;j--){
            if(nums[i] < nums[j]){
                [nums[i], nums[j]] = [nums[j], nums[i]]
                let newnums = nums.slice(i+1, nums.length);
                newnums = newnums.sort((a,b) => a-b);
                // console.log(nums, newnums)
                nums.splice(i+1, nums.length, ...newnums);
                isFinish = true;
                break;
            }
        }
    }
    if(isFinish === false){
        nums = nums.reverse();
    }
};

 
/// 어차피 바꿔야할값은 앞에 작은값 나올때 ! 
function nextPermutation(nums: number[]): void {
    let i = nums.length - 2
    // start at the last 2 nums, find pair out of order (nums[i+1]>nums[i])
    while (i >= 0 && nums[i+1] <= nums[i]) { i-- }
    // if not at beginning of string
    if (i >= 0) {
        let j = nums.length -1 // start at the last num
        // find pair out of order (nums[j]>nums[i])
        while (j >= 0 && nums[j] <= nums[i]) { j-- }
        swap(nums, i, j) // swap out of order numbers
    }
    reverse(nums, i+1) // reverse remaining elements
};

const reverse = (nums: number[], start: number) => {
    let i = start
    let j = nums.length -1
    
    while (i < j) {
        swap(nums, i, j)
        i++
        j--
    }
}

const swap = (nums: number[], i: number, j: number) => {
    let temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
}