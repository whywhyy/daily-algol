/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function (nums, k) {
  const sameValuesArr = new Map();
  nums.forEach((ele, idx) => {
    if (!sameValuesArr.has(ele)) {
      sameValuesArr.set(ele, [idx]);
    } else {
      const arr = sameValuesArr.get(ele);
      arr.push(idx);
    }
  });
  let result = false;
  sameValuesArr.forEach((arr) => {
    if (result === true) {
      return false; // early return 별차이없음
    }
    arr.forEach((val, idx) => {
      if (arr.length - 1 === idx) {
      } else {
        if (Math.abs(arr[idx + 1] - val) <= k) {
          result = true;
        }
      }
    });
  });

  return result;
};

// Time Complexity : O(n)
// Space Complexity : O(n)
var containsNearbyDuplicate = function (nums, k) {
  const hasmap = new Map();
  for (let idx = 0; idx < nums.length; idx++) {
    // Check if the difference betweend duplicates is less than k
    if (idx - hasmap.get(nums[idx]) <= k) {
      return true;
    }
    hasmap.set(nums[idx], idx);
  }
  return false;
};
