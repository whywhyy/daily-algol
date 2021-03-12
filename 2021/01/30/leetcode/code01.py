import heapq
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        nums = [ i *2 if i % 2 == 1 else i for i in nums]
        
        nums.sort()
        nowMax = nums[-1]
        nowMin = nums[0]
        result = nowMax - nowMin

        heap = list(-i for i in nums)
        heapq.heapify(heap)
        while len(heap) > 0:
            now = -heap[0]
            if now < nowMin:
                break
            result = min(result, now - nowMin)
            heapq.heappop(heap)

            if now % 2 == 1:
                break
            nowMin = min(now//2 , nowMin)
            heapq.heappush(heap,-(now//2))

        return result


class Solution:
    def minimumDeviation(self, A: List[int]) -> int:
        pq = []
        for a in A:
            heappush(pq, -a * 2 if a % 2 else -a)
        
        result = float('inf')
        mi = -max(pq)
        while len(pq) == len(A):
            a = -heappop(pq)
            result = min(result, a - mi)
            if a % 2 == 0:
                mi = min(mi, a//2)
                heappush(pq, -a//2)
        return result

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pq = [-2*a if a % 2 == 1 else -a for a in nums]
        cur_min = -max(pq)
        heapify(pq)
        ans = inf
        while pq:
            cur_max = -heappop(pq)
            ans = min(ans, abs(cur_max - cur_min))
            if cur_max % 2 == 1:
                break
            cur_max //= 2
            cur_min = min(cur_max, cur_min)
            heappush(pq, -cur_max)
        return ans