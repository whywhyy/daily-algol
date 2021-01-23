// Find the Most Competitive Subsequence
function mostCompetitive(nums: number[], k: number): number[] {
    let stack = [];
    for(let i=0; i<nums.length; i++){
        if(stack.length === 0){
            stack.push(nums[i]);
        }else{
            while((nums.length-i-1+stack.length >= k) && (stack[stack.length-1] > nums[i])){
                stack.pop()
            }
            if (stack.length < k){
                stack.push(nums[i]);
            }
        }
    }

    return stack;
};

function mostCompetitive(nums: number[], k: number): number[] {
    let result = [];
    result.push(nums[0]);
    let stop: boolean = false;
    
    for (let i = 1; i < nums.length; i++) {
        while (nums[i] < result[result.length - 1]) {
            if (result.length - 1 + (nums.length - i) >= k) {
                result.pop();
            } else {
                stop = true;
                break;
            }
        }
        if (stop === true) {
            return [...result, ...nums.slice(i)];
        } else {
            if (result.length < k) {
                result.push(nums[i]);
            }
        }
    }
    
    return result;
};

function mostCompetitive(nums: number[], k: number): number[] {
    let competiveSequence = [];

    for (let i = 0; i < nums.length;  i++) {               

        // don't do this as it keeps refgerence in while loop
        //let lastElemeent = competiveSequence[competiveSequence.length - 1];
        
        var currentNumber = nums[i];     
        
        while (competiveSequence.length > 0 &&  currentNumber < competiveSequence[competiveSequence.length - 1]) {

            const remainingIterations = nums.length - i;
              
            if ((remainingIterations + competiveSequence.length) > k){
                competiveSequence.pop();
            }    
            
            else {
                break;
            }
        }

        if (competiveSequence.length < k){
          competiveSequence.push(currentNumber);
        }
    }
      
    return competiveSequence;
    
};