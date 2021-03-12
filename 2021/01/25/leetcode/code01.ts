// Check If All 1's Are at Least Length K Places Away
function kLengthApart(nums: number[], k: number): boolean {
    let now = -1;
    for(let i =0;i<nums.length; i++){
        if(nums[i]=== 1){
            now = i
            break
        }
    }

    if(now === -1){
        return true
    }

    for(let i = now+1; i<nums.length; i++){
        if(nums[i] === 1){
            if(i-now-1 <k){
                return false
            }else{
                now = i;
            }
        }
    }

    return true;
};