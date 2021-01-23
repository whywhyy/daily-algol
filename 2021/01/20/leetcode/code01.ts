// Longest Palindromic Substring
// with DP
function longestPalindrome(s: string): string {
    let n = s.length;
    let dp = Array(n);
    for(let i = 0; i<n ; i++){
        dp[i] = Array(n).fill(0);
    }
    
    for(let i=0; i<1; i++){
        for(let j=0; j<n;j++){
            dp[j][j+i] = 1;
        }
    }
    let start = 0;
    let end = 0;
    for(let i=1; i<n; i++){
        for(let j=0; j<n; j++){
            if(s[j] === s[j+i]){
                if (i===1){
                    dp[j][j+i] = 1;
                    start = j
                    end = j+i
                }
                else if(dp[j+1][j+i-1] === 1){
                    dp[j][j+i] = 1;
                    start = j
                    end = j+i
                }
            }
        }
    }
    return s.slice(start,end+1);
};