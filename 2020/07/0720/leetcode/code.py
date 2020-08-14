# problem : Add Binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num_a = self.bin_to_decimal(a)
        num_b = self.bin_to_decimal(b)
        num_a_b = num_a + num_b
        return self.decimal_to_bin(num_a_b)
        
    def bin_to_decimal(self, a:str) -> int:
        if a == "0":
            return 0
        now = 1
        num = 0
        for i in range(len(a)-1,-1,-1):
            if a[i] == '1':
                num += now
            now *=2
        return num

    def decimal_to_bin(self, a:int) -> str:
        result = ""
        if a == 0:
            return "0"
        now_a = a
        while True:
            if now_a == 1 :
                result += '1'
                break
            else :
                if now_a % 2 == 1:
                    result += '1'
                else :
                    result += '0'
            now_a //= 2
        
        return result[::-1]

"""
# 내장함수 이용하여 연산
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return(bin(int(a,2)+int(b,2))[2:])
"""
