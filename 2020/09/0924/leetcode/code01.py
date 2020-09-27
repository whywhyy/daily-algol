# Maximum XOR of Two Numbers in an Array

# https://www.youtube.com/watch?v=wSgrc98d2lI

# tried 자료구조 
# 푸는 방법을 몰라서 헤멨다 ;;
# 정답을 찾아봤는데 봐도 어렵다 ㅠㅠ
# 핵심은 32 비트가 최대이니
# 32비트짜리 수로 바꾸고 해당값을 trie 로 만들기
# tire 로 만들면 가장 큰값을 무조건 찾아가기 때문에 
# 최대값을 찾아가는 것이 확정 ! 
class TrieNode:
    def __init__(self):
        self.children = {}
        
class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    # 0000000000001 
    def insert_bits(self, num):
        bit_num = bin(num)[2:].zfill(32)
        node = self.root
        for bit in bit_num:
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
    
    # 000000000000001
    def find_max_xor(self, num):
        bit_num = bin(num)[2:].zfill(32)
        node = self.root
        max_xor = ''
        for bit in bit_num:
            if bit == '0':
                oppo_bit = '1'
            elif bit == '1':
                oppo_bit = '0'
            
            if oppo_bit in node.children:
                max_xor += oppo_bit
                node = node.children[oppo_bit]
            else:
                max_xor += bit
                node = node.children[bit]
        
        return int(max_xor, 2) ^ num
    
    
    def findMaximumXOR(self, nums: List[int]) -> int:
        for num in nums:
            self.insert_bits(num)
        
        max_ = 0
        for num in nums:
            max_ = max(max_, self.find_max_xor(num))
            
        return max_