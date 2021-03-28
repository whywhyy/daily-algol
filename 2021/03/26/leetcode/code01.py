# Word Subsets
from collections import Counter

class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        inputArr = []
        for i in A:
            inputArr.append(Counter(i))
        

        checkB = Counter([])
        for i in B:
            nowB = Counter(i)
            for word in i:
                checkB[word] = max(checkB[word], nowB[word])
            
        result = []

        for idxA,valA in enumerate(inputArr):
            check = False

            for key in checkB:
                big = valA[key]
                small = checkB[key]
                if(big < small):
                    check = True
                    break

            if(not check):
                result.append(A[idxA])

        return result
        

# good
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        universals = []
        counts = {}
        for word in B:
            for char in word:
                counts[char] = max(counts.get(char, 0), word.count(char))
        
        for word in A:
            for char in counts.keys():
                if word.count(char) < counts[char]:
                    break;
            else:
                universals.append(word)
        return universals