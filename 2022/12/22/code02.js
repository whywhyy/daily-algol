/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  // D[i] = max(D[i-1], D[i-2] + Arr[i])
  let resultArr = new Array(nums.length);
  if (nums.length === 1) {
    return nums[0];
  }
  if (nums.length == 2) {
    return Math.max(nums[0], nums[1]);
  }
  resultArr[0] = nums[0];
  resultArr[1] = Math.max(nums[0], nums[1]);

  for (let i = 2; i < nums.length; i++) {
    resultArr[i] = Math.max(resultArr[i - 1], resultArr[i - 2] + nums[i]);
  }

  return resultArr[nums.length - 1];
};
