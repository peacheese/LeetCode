import enum
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
        while True:
            born = born * 10 + left % 10
            left = left // 10
            if born > left:
                return born // 10 == left
            elif born == left:
                return True  
    #13
    def romanToInt(self, s: str) -> int:
        single_vocab = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        double_vocab = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        i = 0
        target = 0
        while True:
            if i >= len(s):
                break
            if i + 1 < len(s) and s[i] + s[i+1] in double_vocab:
                target += double_vocab[s[i] + s[i+1]]
                i += 2
            else:
                target += single_vocab[s[i]]
                i += 1
        return target
    #219
    def containsNearbyDuplicateI(self, nums: List[int], k: int) -> bool:
        a = {}
        for i, num in enumerate(nums):
            if num not in a:
                a[num] = [i]
            else:
                if i - a[num][len(a[num]) - 1] <= k:
                    return True
                else:
                    a[num].append(i)
        return False
    def containsNearbyDuplicateII(self, nums: List[int], k: int) -> bool:
        a = set()
        begin = 0
        end = min(k, len(nums)-1)
        for i in range(end + 1):
            if nums[i] in a:
                return True
            a.add(nums[i])
        while True:
            end += 1
            if end >= len(nums):
                break
            a.remove(nums[begin])
            begin += 1
            if nums[end] not in a:
                a.add(nums[end])
            else:
                return True
        return False






if __name__ == '__main__':
    solution = Solution()
    print(solution.containsNearbyDuplicateII([1,0,1,1], 1))
