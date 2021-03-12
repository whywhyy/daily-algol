// Number of 1 Bits
function hammingWeight(n: number): number {
    let count = 0;
    while(n){
        n=n&(n-1);
        count++;
    }
    return count;
};


// 그냥 포문이 빠름;;
function hammingWeight(n: number): number {
    const s = n.toString(2);
    let result = 0;
    for (let i = 0; i < s.length; i += 1) {
      result += Number(s[i]);
    }
    return result;
  }