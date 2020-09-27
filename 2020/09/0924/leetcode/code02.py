# Gas Station

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            now_g = gas[i] - cost[i]
            for j in range(1, len(gas)+1):
                now_j = (i+j) % len(gas)
                if now_g < 0:
                    break
                now_g = now_g + gas[now_j] - cost[now_j]

            if now_g >= 0:
                return i
        
        return -1

# 어차피  gas[idx]+fuel <cost[idx] 이면 start 값은 idx+1 임
# 왜냐하면 fuel 은 fuel >= 0 이므로 start = idx + 1 이다 !
# 왜나하면 start - idx 사이에 다시 시작해도 fuel 은 0 으로 시작하기 때문이다. 
# 그리고  sum(gas)<sum(cost) 이면 무조건 -1 이다 ! 
# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:        
#         if sum(gas)<sum(cost):
#             return -1
        
#         start, fuel = 0,0
#         for idx in range(len(gas)):
#             if gas[idx]+fuel <cost[idx]:
#                 start = idx+1 
#                 fuel = 0
#             else :
#                 fuel += gas[idx]- cost[idx]
#         return start

# class Solution:
#     def canCompleteCircuit(self, gas, cost):
#         # O(n) solution. So elegant!
#         n = len(gas)
#         # if there isn't enough gas to cover the cost of trip, no solution exists
#         if n == 0 or sum(gas) < sum(cost):
#             return -1
        
#         # if flow of control is here, solution must exist
#         position = 0
#         balance = 0
#         for i in range(n):
#             # update the amount of fuel we have 
#             balance += gas[i] - cost[i]
#             # if fuel goes negative, that means position or i cannot be
#             # the right answer. Next candidate is i + 1
#             if balance < 0:
#                 position = i + 1
#                 balance = 0
        
#         return position

# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         n = len(gas)
        
#         total_tank, curr_tank = 0, 0
#         starting_station = 0
#         for i in range(n):
#             total_tank += gas[i] - cost[i]
#             curr_tank += gas[i] - cost[i]
#             if curr_tank < 0:
#                 starting_station = i + 1
#                 curr_tank = 0
        
#         return starting_station if total_tank >= 0 else -1