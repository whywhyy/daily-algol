from sortedcontainers import SortedList
# 파이썬 갓 ;;
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        my_arr  = SortedList()
        result = 0
        for i in instructions:
            left = my_arr.bisect_left(i)
            right = len(my_arr) - my_arr.bisect_right(i)
            my_arr.add(i)

            result += min(left,right)
            result %= 10**9 + 7
        return result 
        
# 
class Solution:
    def createSortedArray(self, A):
        m = max(A)
        c = [0] * (m + 1)

        def update(x):
            while (x <= m):
                c[x] += 1
                x += x & -x

        def get(x):
            res = 0
            while (x > 0):
                res += c[x]
                x -= x & -x
            return res

        res = 0
        for i, a in enumerate(A):
            res += min(get(a - 1), i - get(a))
            update(a)
        return res % (10**9 + 7)

'''
// typescrpt 실패 
// Create Sorted Array through Instructions
// time limit 
function createSortedArray(instructions: number[]): number {
    let num : Map<number,number> = new Map();
    let result : number = 0;
    let mod : number = 10**9 + 7;

    instructions.forEach((v) => {
        let count = num.has(v) ? num.get(v) : 0;
        num.set(v, count+1)
        let left : number = 0;
        let right : number = 0;

        num.forEach((value, key) => {
            if(v !== key){
                if (v < key){
                    right += value;
                }else{
                    left +=  value;
                }
            }
        });
        
        result += Math.min(left,right);
        result %= mod;
    });

    return result 
}
'''
