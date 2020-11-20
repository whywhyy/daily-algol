# Consecutive Characters
class Solution:
    def maxPower(self, s: str) -> int:
        
        now_max = 1
        now_count = 1

        now_char = s[0]
        for i in range(1, len(s)) :
            if now_char == s[i]:
                now_count += 1
                now_max = max(now_count, now_max)
            else:
                now_count = 1
                now_char = s[i]

        return now_max