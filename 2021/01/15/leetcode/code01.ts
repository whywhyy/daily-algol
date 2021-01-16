// Get Maximum in Generated Array

function getMaximumGenerated(n: number): number {
    let result : Array<number> = [];
    result.push(0);
    result.push(1);

    if(n===0){
        return 0;
    }

    let maxResult = 1
    for(let i=2; i<n+1; i++){
        let even =i/2;
        let oddFront =  (i-1)/2;
        let oddBack = (i-1)/2 + 1;

        const input = i%2 ? result[oddFront]+result[oddBack] : result[even];
        result.push(input);
        maxResult = maxResult > input ? maxResult : input;
    }
    return maxResult;
};


// for문 내에서 매번 연산하는 것보다
// 그냥 전체 받아서 max 찾는게 더 빠름. !!?
function getMaximumGenerated(n: number): number {
    if(n === 0) {
        return 0;
    } 
    /*
    else if(n === 1) {
        return 1;
    }
    */
    
    const nums: number[] = [0,1];
    
    
    for(let iN = 1; iN < 0.5 * n; iN++) {
        nums[2 * iN] = nums[iN];
        nums[2 * iN + 1] = nums[iN] + nums[iN + 1];
    }
    
    return Math.max(...nums);
};