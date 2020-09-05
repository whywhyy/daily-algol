#  Partition Labels
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        result = []

        count = 0
        prev_i = 0
        for i in range(len(S)):
            if prev_i == 0:
                prev_i = S.rfind(S[i])
                count = 1 
                if prev_i == i:
                    prev_i = 0
                    result.append(count)
            else:
                if prev_i == i:
                    count += 1
                    result.append(count)
                    count = 0
                    prev_i = 0
                    continue
                else:
                    if prev_i < S.rfind(S[i]):
                        prev_i = S.rfind(S[i])
                        count += 1
                    else:
                        count +=1 

        return result


# # AWESOME
# # dict 로 last index 구함 !
# # max(end, end_idx[letter]) 을 이용하여 적절하게 end 를 구한다!
# # #
# class Solution:
#     def partitionLabels(self, S: str):

#         end_idx = {s: i for i, s in enumerate(S)}
#         start = 0
#         end = 0

#         result = []
#         for i, letter in enumerate(S):
#             end = max(end, end_idx[letter])
#             if i == end:
#                 result.append(end - start + 1)
#                 start = i + 1
                
#         return result

