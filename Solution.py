from functools import cmp_to_key
from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
    #539
    def findMinDifference(self, timePoints: List[str]) -> int:
        def cmp(time1, time2):
            t1 = time1.split(':')
            t2 = time2.split(':')
            if int(t1[0]) > int(t2[0]):
                return 1
            elif int(t1[0]) < int(t2[0]):
                return -1
            else:
                if int(t1[1]) > int(t2[1]):
                    return 1
                else: 
                    return -1
        def diff(time1, time2):
            t1 = time1.split(':')
            t2 = time2.split(':')
            return 60 * (int(t2[0]) - int(t1[0])) + (int(t2[1]) - int(t1[1]))
        if len(timePoints) > 1440:
            return 0
        timePoints.sort(key=cmp_to_key(cmp))
        print(timePoints)
        target = 1 << 31 
        for i, item in enumerate(timePoints):
            if i + 1 < len(timePoints):
                dif = diff(timePoints[i], timePoints[i+1])
            else:
                dif = 24 * 60 - diff(timePoints[0], timePoints[i]) 
            target = dif if dif < target else target
        return target
    #2
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tgt = ListNode()
        prev = None
        now = tgt
        l1HasNext = True
        l2HasNext = True
        while True:
            if l1HasNext and l2HasNext:
                now.next = ListNode()
                now.next.val += (now.val + l1.val + l2.val) // 10
                now.val = (now.val + l1.val + l2.val) % 10
                prev = now
                now = now.next
            elif l1HasNext:
                now.next = ListNode()
                now.next.val += (now.val + l1.val) // 10
                now.val = (now.val + l1.val) % 10
                prev = now
                now = now.next
            elif l2HasNext:
                now.next = ListNode()
                now.next.val += (now.val + l2.val) // 10
                now.val = (now.val + l2.val) % 10
                prev = now
                now = now.next
            else:
                if now.val == 0:
                    prev.next = None
                break
            if not l1.next:
                l1HasNext = False
            else:
                l1 = l1.next
            if not l2.next:
                l2HasNext = False
            else:
                l2 = l2.next
        return tgt
    #14
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def commonPrefix(s1, s2):
            prefix = ''
            length = min(len(s1), len(s2))
            for i in range(length):
                if s1[i] == s2[i]:
                    prefix += s1[i]
                else:
                    break
            return prefix
        if len(strs) == 1:
            return strs[0]
        elif len(strs) == 2:
            return commonPrefix(strs[0], strs[1])
        else:
            return commonPrefix(self.longestCommonPrefix(strs[0: len(strs) // 2]), self.longestCommonPrefix(strs[len(strs) // 2: len(strs)]))
    #20
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        left = ['(', '[', '{']
        match = {')':'(', ']':'[', '}':'{'}
        for ch in s:
            if ch in left:
                stack.append(ch)
            else:
                if len(stack) == 0 or match[ch] != stack.pop():
                    return False
        return True if len(stack) == 0 else False
    #3
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        window = [s[0]]
        maxlen = 1
        end = 0
        while True:
            if end == len(s) - 1:
                break
            if s[end + 1] not in window:
                end += 1
                window.append(s[end])
                maxlen = len(window) if maxlen < len(window) else maxlen
            else:
                del(window[0])
        return maxlen
    #21
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode()
        now = prev
        while list1 and list2:
            if list1.val < list2.val:
                now.next = list1
                now = now.next
                list1 = list1.next
            else:
                now.next = list2
                now = now.next
                list2 = list2.next
        now.next = list1 if list1 else list2 if list2 else None
        return prev.next
    #26
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for num in nums:
            if num != nums[i]:
                i += 1
                nums[i] = num
        return i + 1
    #27
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i
    #5
    def longestPalindrome(self, s: str) -> str:
        maxlen = 0
        maxpalind = ''
        for i, ch in enumerate(s):
            begin = i
            end = i
            palind = ch
            while True:
                if 0 < begin and end < len(s) - 1:
                    begin -= 1
                    end += 1
                    if s[begin] == s[end]:
                        palind = s[begin] + palind + s[end]  
                    else:
                        break
                else:
                    break
            print(palind)
            if len(palind) > maxlen:
                maxlen = len(palind)
                maxpalind = palind
            if i < len(s) - 1 and s[i + 1] == ch:
                begin = i
                end = i + 1
                palind = ch + ch
                while True:
                    if 0 < begin and end < len(s) - 1:
                        begin -= 1
                        end += 1
                        if s[begin] == s[end]:
                            palind = s[begin] + palind + s[end]  
                        else:
                            break
                    else:
                        break
                if len(palind) > maxlen:
                    maxlen = len(palind)
                    maxpalind = palind
            print(palind)
        return maxpalind
    #28
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)
        pass
    #35
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if target <= nums[0] else 1
        if nums[len(nums) // 2] < target:
            return len(nums) // 2 + self.searchInsert(nums[len(nums) // 2 : len(nums)], target)
        else:
            return self.searchInsert(nums[0 : len(nums) // 2], target)
    



if __name__ == '__main__':
    solution = Solution()
    print(solution.searchInsert([1], 0))

