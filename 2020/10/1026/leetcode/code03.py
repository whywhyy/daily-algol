# Bag of Tokens
from collections import deque
class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens = sorted(tokens)
        tokens = deque(tokens)
        
        result = 0
        now_p = P
        while tokens and tokens[0] <= now_p:
            now_p -= tokens.popleft()
            result += 1
            if len(tokens) > 1 and now_p < tokens[0]:
                now_p += tokens.pop()
                result -= 1

        return result

# cursur 을 이용하여 잘 구현하였다.
# cursur 로 구현하는 습관도 좋은것같다 ! 
# 최소 1포인트는 확보를 확인하고 시작.
class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        if not tokens or P < tokens[0]:
            return 0
        score = 0
        left, right = 0, len(tokens) - 1
        while left <= right:
            if P >= tokens[left]:
                P -= tokens[left]
                left += 1
                score += 1
            else:
                if right - left > 1:
                    P += tokens[right]
                    right -= 1
                    score -= 1
                else:
                    break
        return score