// Max Number of K-Sum Pairs
function maxOperations(nums: number[], k: number): number {
    let result = 0;

    nums.sort((a,b) => a-b)
    let start = 0;
    let end = nums.length - 1;
    while (start < end){
        let now = nums[start] + nums[end];
        if(now == k){
            result+=1;
            start +=1;
            end -=1;
        }else if (now < k){
            start += 1;
        }else{
            end -=1;
        }
    }
    return result;
};

// 
function maxOperations(nums: number[], k: number): number {
    const map = new Map<number, number>()
    let ans = 0
    for (const n of nums) {
        const count = map.get(k - n) || 0
        if (count > 0) {
            map.set(k - n, count - 1)
            ans += 1
        } else {
            map.set(n, (map.get(n) || 0) + 1)
        }
    }
    return ans
}

function maxOperations(nums: number[], k: number): number {
    const seenCount = new Map();
    
    let ans = 0;
    for (let n of nums) {
        // seen + n === k => seen = k - n
        //console.log(seenCount)
        const maybeSeen = k - n;
        if (maybeSeen > 0 && seenCount.has(maybeSeen) && seenCount.get(maybeSeen) > 0) {
            ans++;
            seenCount.set(maybeSeen, seenCount.get(maybeSeen) - 1)
        } else {
            seenCount.set(n, (seenCount.get(n) || 0) + 1)
        }
    }
    
    return ans;
};