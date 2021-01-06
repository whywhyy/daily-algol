# 4Sum II
from collections import defaultdict
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        result = 0
        # A + B 
        # C + D
        ab_sum = defaultdict(int)
        cd_sum = defaultdict(int)

        for i in A:
            for j in B:
                ab_sum[i+j] += 1

        for i in C:
            for j in D:
                cd_sum[i+j] += 1

        for i in ab_sum:
            if cd_sum[-i]:
                result += ab_sum[i] * cd_sum[-i]

        return result

# 4Sum II
# 살짝 개선 with Counter
from collections import defaultdict
from collections import Counter
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        result = 0
        # A + B 
        # C + D
        ab_sum = defaultdict(int)
        cd_sum = defaultdict(int)

        A = Counter(A)
        B = Counter(B)
        for i in A:
            for j in B:
                ab_sum[i+j] += A[i] * B[j]

        C = Counter(C)
        D = Counter(D)
        for i in C:
            for j in D:
                cd_sum[i+j] += C[i] * D[j]

        low_len = ab_sum if len(ab_sum) <= len(cd_sum) else cd_sum
        long_len = ab_sum if len(ab_sum) > len(cd_sum) else cd_sum

        for i in low_len:
            if long_len[-i]:
                result += low_len[i] * long_len[-i]
        

        return result

# AB 계산후 CD 계산할때 결과 output
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        hashtable = {}
        for a in A:
            for b in B:
                if a+b in hashtable:
                    hashtable[a+b] += 1
                else:
                    hashtable[a+b] = 1
        
        ans = 0
        
        for c in C:
            for d in D:
                if -c-d in hashtable:
                    ans += hashtable[-c-d]
        
        return ans

# 이중 for AND Counter !
# count_ab[-c-d] 의 갯수의 합 ?!
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        count_ab = collections.Counter(a + b for a in A for b in B)
        res = sum(count_ab[- c - d] for c in C for d in D)
        return res


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        
        sol = 0
        
        A2 = {}
        B2 = {}
        C2 = {}
        D2 = {}
        
        twoSumX = {}
        twoSumXX = {}
        
        for i in A:
            if A2.get(i) == None:
                A2[i] = 1
            else:
                A2[i] += 1
        for i in B:
            if B2.get(i) == None:
                B2[i] = 1
            else:
                B2[i] += 1
        for i in C:
            if C2.get(i) == None:
                C2[i] = 1
            else:
                C2[i] += 1
        for i in D:
            if D2.get(i) == None:
                D2[i] = 1
            else:
                D2[i] += 1
        
        for i in A2:
            for j in B2:
                if twoSumX.get(i + j) == None:
                    twoSumX[i + j] = A2[i] * B2[j]
                else:
                    twoSumX[i + j] += A2[i] * B2[j]

        for i in C2:
            for j in D2:
                if -(i + j) in twoSumX:
                    sol += twoSumX[-(i + j)] * C2[i] * D2[j]
                
        
        return sol