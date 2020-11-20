# Decode String
class Solution:
    def decodeString(self, s: str) -> str:
    
        stack = []
        for i in s:
            if not stack:
                stack.append(i)
            else:
                if i.isdigit():
                    if stack[-1].isdigit():
                         stack[-1] += i
                    else:
                        stack.append(i)
                else:
                    if i == '[':
                        stack.append(i)
                    elif i == ']':
                        now_str = stack.pop()
                        _ = stack.pop()
                        now_num = stack.pop()
                        now_str *= int(now_num)

                        new_str = ""
                        while stack and stack[-1] != '[' and stack[-1] !=']':
                            new_str += stack.pop()
                        stack.append(new_str + now_str)
                    else:
                        if stack[-1] != '[':
                            stack[-1] += i
                        else:
                            stack.append(i)

        return "".join(stack[-1])

# stack[-1][0] 번째에 해당하는 string 을 넣는다!
# ']' 가 나오면 pop, st num 값과 함께 계산 !
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        stack.append(["", 1])
        num = ""
        for ch in s:
            if ch.isdigit():
              num += ch
            elif ch == '[':
                stack.append(["", int(num)])
                num = ""
            elif ch == ']':
                st, k = stack.pop()
                stack[-1][0] += st*k
            else:
                stack[-1][0] += ch
        return stack[0][0]


class Solution:
    def decodeString(self, s: str) -> str:
        cur_str, cur_num, stack = '', 0, []
        for c in s:
            if c == '[':
                stack.append(cur_str)
                stack.append(cur_num)
                cur_str = ''
                cur_num = 0
            elif c == ']':
                num = stack.pop()
                pre_str = stack.pop()
                cur_str = pre_str + num * cur_str
            elif c.isdigit():
                cur_num = cur_num * 10 + int(c)
            else:
                cur_str += c
        return cur_str

class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        for i, _s in enumerate(s):
            if len(stack) == 0:
                stack.append(_s)
            else:
                if _s.isnumeric() and stack[-1].isnumeric():
                    stack[-1] = str(int(stack[-1])*10 + int(_s))
                elif _s.isnumeric() and not stack[-1].isnumeric():
                    stack.append(_s)
                elif _s == '[':
                    stack.append(_s)
                elif _s.isalpha():
                    if stack[-1].isalpha():
                        stack[-1] = stack[-1] + _s
                    else:
                        stack.append(_s)
                elif _s == ']':
                    
                    word = stack[-1]
                    del stack[-1]    # del word
                    del stack[-1]    # del [
                    number = int(stack[-1])
                    del stack [-1]   # del number
                    
                    new_word = []
                    while number:
                        new_word.append(word)
                        number -= 1
                    word_to_append = "".join(new_word)
                    
                    if len(stack) == 0:
                        stack.append(word_to_append)
                    elif stack[-1].isalpha():
                        stack[-1] = stack[-1] + word_to_append
                    else:
                        stack.append(word_to_append)
        
        return stack[0]


# ']' 가 나왔을때 쭉 처리!!
# temp_str, num 만들어서 계산 후 stack 에 저장!
# 
class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        res = []
        
        for char in s:
            if char == ']':
                tmpStr = []
                k = 0
                base = 0
                while stack[-1] != '[':
                    tmpStr.append(stack.pop())
                stack.pop()
                while stack and stack[-1].isnumeric():
                    num = stack.pop()
                    k += (ord(num) - ord('0')) * (10 ** base)
                    base += 1
                for _ in range(k):
                    for i in range(len(tmpStr) - 1, -1, -1):
                        stack.append(tmpStr[i])
            else:
                stack.append(char)
        
        return  ''.join(stack)