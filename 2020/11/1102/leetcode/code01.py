# Maximize Distance to Closest Person
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_dis = 0
        
        stack_dis = []
        for i in range(len(seats)):
            if seats[i] == 1:
                stack_dis.append(i+1)


        for i in range(len(stack_dis)-1):
            max_dis = max(max_dis, stack_dis[i+1] - stack_dis[i])

        return max(max_dis//2, stack_dis[0]-1, len(seats)-stack_dis[-1])

# 1 일때 예외처리 
# last 값 예외처리
class Solution:
    def maxDistToClosest(self, seats: List[int]):
        start = -1
        maxgap = 0
        
        for i in range(len(seats)):
            if seats[i] == 1:
                #is there a person sitting there?
                if start == -1: 
                    maxgap = i
                   #first person (p1) 
                else: 
                    maxgap = max(maxgap, (i-start)//2)
                    #this is second person
                    #can we sit in between?
                    #if so is it better than our current best option?
                
                start = i
         # Check the last seat it it is empty could be the best choice.
        maxgap = max(maxgap, len(seats)-1-start)
        
        return maxgap

# 0의 개수이므로 ceil(count/2) 로 구함
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        distance = 0
        
        start = True
        count = 0
        for i in range(len(seats)):
            if seats[i] == 0:
                count +=1
            else:
                if start:
                    distance = max(distance, count)
                    start = False
                else:
                    distance = max(distance, ceil(count/2))
                count = 0
        distance = max(distance, count)
        return distance

# 첫번째 자리 예외처리
# prev 좌석 저장
# (idx - prev) /2  로 중간 좌석 길이 결정
# 마직자리 예외처리 : len(seats) - 1 - prev 로 결정
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        last_taken_seat = -1
        max_dist = 0
        for i, curr_seat in enumerate(seats):
            if not curr_seat:
                continue
            if last_taken_seat == -1:
                # Alex cannot sit, don't update anything
                if i != 0:
                    # otherwise sit on the first one which maximizes distance.
                    max_dist = i
            else:
                if i - last_taken_seat > 1:
                    max_dist = max(max_dist, (i - last_taken_seat) / 2)
            last_taken_seat = i
        # Check the last seat it it is empty could be the best choice.
        if not seats[-1]:
            max_dist = max(max_dist, len(seats) - 1 - last_taken_seat)
        return int(max_dist)

# 나와 동일한 컨셉
# 다만 array 를 사용하지 않고 해결 !
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        prev = None
        diff = 0
        result = -1
        
        n = len(seats)
        for i in range(n):
            if seats[i]:
                if prev is None:
                    prev = i
                    left = i
                elif i-prev > diff:
                    diff = i-prev
                    result = diff // 2
                prev = i
        
        right = n - prev - 1
        
        return max(left, right, result)