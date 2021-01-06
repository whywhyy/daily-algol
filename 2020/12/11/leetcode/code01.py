# Valid Mountain Array
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        idx = 0
        n = len(arr)
        while idx < n-1 and arr[idx] < arr[idx+1]:
            idx += 1
        
        if idx == 0 or idx == n-1:
            return False

        while idx < n-1 and arr[idx] > arr[idx+1]:
            idx += 1

        return True if idx == n-1 else False

# 3개 false
# top 이 같은지 확인!
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        for i in range(len(arr)-1):
            if arr[i] >= arr[i+1]:
                break
        
        for j in reversed(range(1, len(arr))):
            if arr[j-1] <= arr[j]:
                break
        
        if i == j:
            return True
        else:
            return False

# 
class Solution:
    def validMountainArray(self, a):
        ascend = True
        descend = False
        
        i = 0
        l = len(a)
        
        if l == 1:
            return False
        
        while (i < l-1):
            if ascend and a[i] < a[i+1]:
                i += 1
                continue
            else:
                if i == 0:
                    return False
                descend = True
                ascend = False
                if a[i] > a[i+1]:
                    i += 1
                    continue
                else:
                    return False
        if descend:
            return True
        else:
            return False

# return 부분을 0 < i == j < n - 1 로 정의 !
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A)<3:
            return False
        i, j, n = 0, len(A) - 1, len(A)
        while i + 1 < n and A[i] < A[i + 1]: 
            i += 1
        while j > 0 and A[j - 1] > A[j]: 
            j -= 1
        return 0 < i == j < n - 1

# top 나올시 uphill = False
# downhill 시 arr[i-1] <= arr[i]: return False
# return not uphill 로 리턴!
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3 or arr[0]>=arr[1]:
            return False
			
        uphill = True
        
        for i in range(1,len(arr)):
            if uphill:
                if arr[i-1]>=arr[i]:
                    uphill = False
            if not uphill:
                if arr[i-1]<=arr[i]:
                    return False
        return not uphill

# up and down 이후 if i == j and i != 0 and j != len(arr)-1:
# 로 정의
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) < 3:
            return False
    
        i, j = 0, len(arr)-1

        while i < len(arr)-1 and arr[i+1] > arr[i]:
            i += 1

        while j >= 0 and arr[j] < arr[j-1]:
	        j -= 1

        if i == j and i != 0 and j != len(arr)-1:
	        return True
        return False

# top 만 확인후 down 진행하기
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3: return False
        top, bottom = 0, 0
        for i in range(1, n):
            if arr[i] <= arr[i-1]:
                top = i-1
                break
        if top in (0, n-1): 
            return False
        for i in range(top+1, n):
            if arr[i] >= arr[i-1]:
                return False
        return True

# top 갯수를 k로 정의한듯!?
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        n = len(A)
        if n < 3: return False
        inc = A[0] < A[1]
        k = 0
        for i in range(1, n):
            if inc and A[i-1] >= A[i]: 
                k += 1
                inc = False
            if not inc and A[i-1] <= A[i]:
                return False
        return k == 1