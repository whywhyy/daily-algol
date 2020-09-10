#  Compare Version Numbers
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        
        if len(version1) >= len(version2):
            long_ver = version1
            sm_ver = version2
        else:
            long_ver = version2
            sm_ver = version1

        for i in range(len(sm_ver)):
            if int(long_ver[i]) == int(sm_ver[i]):
                continue
            else:
                if int(long_ver[i]) > int(sm_ver[i]):
                    if len(version1) >= len(version2):
                        return 1
                    else:
                        return -1
                else:
                    if len(version1) >= len(version2):
                        return -1
                    else:
                        return 1
        if len(version1) == len(version2):
            return 0
        
        else: 
            for i in range(len(sm_ver),len(long_ver)):
                if int(long_ver[i]) > 0:
                    if len(version1) >= len(version2):
                        return 1
                    else:
                        return -1
            return 0

# # awesome
# # 그저 감탄
# # 읽는데도 한참 걸린 ㅠㅠ..
# class Solution:
#     def compareVersion(self, version1: str, version2: str) -> int:
#         v1=version1
#         v2=version2
#         v1, v2 = map(int, v1.split('.')), map(int, v2.split('.'))
#         v1, v2 = zip(*zip_longest(v1, v2, fillvalue = 0))
#         # 7.5.2.4 / 7.5.3
#         # (7,5,2,4)   (7,5,3,0)
#         print(v1, v2)
#         # True - False = 1
#         # False - True = -1 
#         # Fale - False = 0
# https://docs.python.org/3/tutorial/datastructures.html#comparing-sequences-and-other-types
# 
#         print([(v1 > v2) - (v1 < v2)])
#         return (0, 1, -1)[(v1 > v2) - (v1 < v2)]

# # 따로 longest 를 찾지 않고
# # if i>= len(v1) : if int(v2[i]): -1 이런식으로
# # 잘 정의 했다 !
# # 끝까지 동일할경우 return 0 !
# class Solution:
#     def compareVersion(self, version1: str, version2: str) -> int:
#         v1, v2 = version1.split('.'), version2.split('.')
#         i = 0
        
#         while i < max(len(v1), len(v2)):
#             if i >= len(v1):
#                 if int(v2[i]):
#                     return -1
#             elif i >= len(v2):
#                 if int(v1[i]):
#                     return 1
#             else:
#                 n1, n2 = int(v1[i]), int(v2[i])
#                 if n1 > n2:
#                     return 1
#                 elif n1 < n2:
#                     return -1
#             i += 1
            
#         return 0

# # 위의 코드보다 조금더 정돈된 느낌!
# class Solution:
#     def compareVersion(self, version1: str, version2: str) -> int:
#         nums1 = version1.split('.')
#         nums2 = version2.split('.')
#         n1, n2 = len(nums1), len(nums2)
        
#         # compare versions
#         for i in range(max(n1, n2)):
#             i1 = int(nums1[i]) if i < n1 else 0
#             i2 = int(nums2[i]) if i < n2 else 0
#             print(i1, i2)
#             if i1 != i2:
#                 return 1 if i1 > i2 else -1
        
#         # the versions are equal
#         return 0 