// Longest Substring Without Repeating Characters

function lengthOfLongestSubstring(s: string): number {
    let result : number = 0;
    let check : string[] = [];
    for(let i : number = 0; i < s.length; i++){
        if(check.some(x=>x==s[i])){
            check = check.slice(check.indexOf(s[i])+1);
        }
        check.push(s[i]);
        result = Math.max(result, check.length);
    }
    return result
};


// include 함수 -> 포함하는지 확인함
function lengthOfLongestSubstring(s: string): number {
    if (s.length === 0) {
      return 0;
    }
  
    let letters = s.split('');
    let substring: string[] = [];
    let maxSubstringLength = 0;
  
    while (letters.length) {
      const letter = letters.pop();
  
      if (letter === undefined) {
        break;
      }
  
      if (substring.includes(letter)) {
        if (maxSubstringLength < substring.length) {
          maxSubstringLength = substring.length;
        }
  
        const start = substring.indexOf(letter);
        substring = substring.slice(start + 1);
      }
  
      substring.push(letter);
    }
  
    return substring.length < maxSubstringLength ? maxSubstringLength : substring.length;
  }

// map type => dict key,value 형태
// lptr : 현재 char와 동일한 값의 위치
// 앞에 존재하나 lptr 보다 작으면 skip
function lengthOfLongestSubstring(s: string): number {
    const map = new Map()
    let result = 0, lptr=0, rptr=0
    
    if(!s.length){
       return 0
    }
    
    for(let rptr=0; rptr<s.length; rptr++){
        if(map.has(s[rptr])){
            let pos = map.get(s[rptr])+1
            lptr = pos > lptr ? pos : lptr
        }
        map.set(s[rptr], rptr)
        result = Math.max( result, rptr-lptr+1 )
    }

    return result
};


// s[j] 가 delete 될때까지 s[i] 삭제 ! 
function lengthOfLongestSubstring(s: string): number {
    //eg: abcabcbb
	let i: number = 0;
	let j: number = 0; //both pointers start at "a"
	let max: number = 0; //keep track of the longest substr length so far
	const set = new Set();

	while (j < s.length) {
		if (!set.has(s[j])) {
			//if the char is unique, add it to the set --set only contains unique chars
			set.add(s[j]);
			max = Math.max(max, set.size);
			j += 1;
		} else {
			//if char is already in the set, then remove it
			set.delete(s[i]);
			i += 1;
		}
	}

	return max;
};

// entries ?? => index, value ! 
// i = Math.max(map.get(jValue) , i); 
// : 앞에 있으면서 현재의 i 값보다 뒤에있는지 확인
function lengthOfLongestSubstring(s: string): number {
    let ans: number = 0, i: number = 0;
    let map = new Map();
  
    for (let [j, jValue] of [...s].entries()) {
      if (!map.has(jValue)) {
        map.set(jValue, j + 1);
        ans = Math.max(ans, j - i + 1);
      } else {
        i = Math.max(map.get(jValue) , i);
        map.set(jValue, j + 1);
        ans = Math.max(ans, j - i + 1);
      }
    }
    return ans;
  }