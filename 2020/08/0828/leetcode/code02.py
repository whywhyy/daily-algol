# Fizz Buzz

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = [str(i+1) for i in range(n)]

        for i in range(n//3):
            result[(i+1)*3-1] = "Fizz"
        for i in range(n//5):
            if result[(i+1)*5-1] == "Fizz":
                result[(i+1)*5-1] += "Buzz"
            else:
                result[(i+1)*5-1] = "Buzz"

        return result

# # append 로 해도 속도는 빠르다.
# # if not i%15 로 해서 괜찮은 코드 같다.
# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:
#         out = []
#         for i in range(1, n+1):
#             if not (i % 15):
#                 out.append('FizzBuzz')
#             elif not (i % 5):
#                 out.append('Buzz')
#             elif not (i % 3):
#                 out.append('Fizz')
#             else:
#                 out.append(str(i))
#         return out

# # 시도하려다 못한 코드인데
# # True False 을 곱한다 !;;
# # awesome!
# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:
#         return ['Fizz'*(i%3==0) + 'Buzz'*(i%5==0) or str(i) for i in range(1,n+1)]