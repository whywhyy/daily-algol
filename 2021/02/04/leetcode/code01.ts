// Longest Harmonious Subsequence
function findLHS(nums: number[]): number {
    let maps = new Map();
    for(let i=0; i<nums.length; i++){
        const now = nums[i];
        if(maps.has(now)){
            maps.set(now, maps.get(now)+1);
        }else{
            maps.set(now,1);
        }
    }
    let result = 0;
    for(let i=0; i<nums.length; i++){
        if(maps.has(nums[i]) && maps.has(nums[i]+1)){
            result = Math.max(result, maps.get(nums[i])+ maps.get(nums[i]+1))
        }
    }

    return result;
};

// 코드 깔끔 데스
function findLHS(nums: number[]): number {
    const map = new Map<number, number>();
    
    // good
    for (let n of nums) {
        map.set(n, (map.get(n) || 0) + 1); 
    }
    
    let result = 0;
    
    // good
    for (let [key, value] of map) {
        if (map.has(key + 1)) {
            result = Math.max(result, value + map.get(key + 1));
        }
    }
    
    return result;
};