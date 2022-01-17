from typing import List

class Solution:
    #1
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        a = {}
        for i, num in enumerate(nums):
            if target - num not in a:
                a[num] = i
            else:
                return [i, a[target - num]]
    #9
    def isPalindromeI(self, x: int) -> bool:
        num = str(x)
        for i in range((len(num) + 1) // 2):
            if num[i] != num[len(num) - i - 1]:
                return False
        return True
    def isPalindromeII(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        left = x
        born = 0
        
        



             
if __name__ == '__main__':
    solution = Solution()
