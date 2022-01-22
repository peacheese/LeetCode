## LeetCode

#### [1. 两数之和](https://leetcode-cn.com/problems/two-sum/)

给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 **和为目标值** `target`  的那 **两个** 整数，并返回它们的数组下标。

解：降低复杂度，需要用到字典 `dict` 来解法，因为字典是哈希表，O(1) 时间复杂度，每次查找目标因为知道了要找的目标的值，就可以考虑用 key/val 形式来进行查找，其中 val 就是数组对应的下标。而不需要遍历 val 来查找 key，这样只需要遍历一遍，注意不能和自身查找，这个问题就是类似于第 i 个遍历前面 i-1 个的问题，开始是空字典，边查找边加进去就可以了，实际上因为是组合只要找 O(n*n/2) ，应该先查找，找不到再把自己加到字典中去。

#### [9. 回文数](https://leetcode-cn.com/problems/palindrome-number/)

给你一个整数 `x` ，如果 `x` 是一个回文整数，返回 `true` ；否则，返回 `false` 。

解：我用字符串解得，占得空间比较大，题解的方法是将后面的数变到前面，这种方法只需要常量空间就可以，判断是否达到一半长度也很巧妙，用原来的数和新的数进行比较大小就可以，因为位数不同一定有大小之分，注意开始的时候要处理几种特殊情况。

#### [13. 罗马数字转整数](https://leetcode-cn.com/problems/roman-to-integer/)

罗马数字包含以下七种字符: `I`， `V`， `X`， `L`，`C`，`D` 和 `M`。

```
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

例如， 罗马数字 `2` 写做 `II` ，即为两个并列的 1 。`12` 写做 `XII` ，即为 `X` + `II` 。 `27` 写做 `XXVII`, 即为 `XX` + `V` + `II` 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 `IIII`，而是 `IV`。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 `IX`。这个特殊的规则只适用于以下六种情况：

- `I` 可以放在 `V` (5) 和 `X` (10) 的左边，来表示 4 和 9。
- `X` 可以放在 `L` (50) 和 `C` (100) 的左边，来表示 40 和 90。 
- `C` 可以放在 `D` (500) 和 `M` (1000) 的左边，来表示 400 和 900。

给定一个罗马数字，将其转换成整数。

解：简单，用哈希表，我用了两个，其实只需要用一个，判断下一个数的大小然后取反就可以了。

#### [219. 存在重复元素 II](https://leetcode-cn.com/problems/contains-duplicate-ii/)

给你一个整数数组 `nums` 和一个整数 `k` ，判断数组中是否存在两个 **不同的索引** `i` 和 `j` ，满足 `nums[i] == nums[j]` 且 `abs(i - j) <= k` 。如果存在，返回 `true` ；否则，返回 `false` 。

解：滑动窗口大法，好。尤其是下标 <= k 这种，用 `set` 来搞就可以。我之前用的字典，空间没有优势，注意初始化窗口，或者就从 0 的小窗口开始加到 k 大小再滑动，比如初始 [0, 0] -> [0, 1] -> ... -> [0,5] -> [1,6] -> [2,7] 这样。

#### [539. 最小时间差](https://leetcode-cn.com/problems/minimum-time-difference/)

给定一个 24 小时制（小时:分钟 **"HH:MM"**）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。

解：鸽巢原理。我是什么fw，没想到，以及世界上真的只有我以为不能直接 sort 然后手写了 cmp 吗。

#### [2. 两数相加](https://leetcode-cn.com/problems/add-two-numbers/)

给你两个 **非空** 的链表，表示两个非负的整数。它们每位数字都是按照 **逆序** 的方式存储的，并且每个节点只能存储 **一位** 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

解：一般的链表遍历，遍历就好，但是这种题最容易出错，尽量细心点，貌似我多用了很多空间，懒得改了。

#### [14. 最长公共前缀](https://leetcode-cn.com/problems/longest-common-prefix/)

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 `""`。

解：本以为是简单的分治问题，递归解了。看到评论才知道我是什么废物，直接用 min，max 对字符串数组排序取最大和最小然后比较就可以了，因为是按 ascii 排的所以最大最小的公共前缀就是最大公共前缀。还有另外一种解法要用到 `zip()` 函数，记录一下使用：

```
>>>a = [1,2,3]
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zipped = zip(a,b)     # 打包为元组的列表
[(1, 4), (2, 5), (3, 6)]
>>> zip(a,c)              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]
>>> zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
[(1, 2, 3), (4, 5, 6)]
>>> list(zip(*zipped))    # python3 以后返回对象，要用 list 进行处理
```

以及集合去重：`map()` 会根据提供的函数对指定序列做映射。第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
这道题里面巧妙在用 `zip()` 函数解压，相当于把一个字符串的一维数组看做二维数组进行解压，然后解压得到的数组每个元素都是原来字符串相同位置对应的字符们，然后再用 set 进行去重，解法：

```python
def longestCommonPrefix(self, strs):
  if not strs: return ""
  ss = list(map(set, zip(*strs))) 
  res = ""
  for i, x in enumerate(ss):
    x = list(x)
    if len(x) > 1:
      break
      res = res + x[0]
      return res
```

#### [20. 有效的括号](https://leetcode-cn.com/problems/valid-parentheses/)

给定一个只包括 `'('`，`')'`，`'{'`，`'}'`，`'['`，`']'` 的字符串 `s` ，判断字符串是否有效。

有效字符串需满足：

1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。

解：栈，简单死了，但是为何我还是没有考虑到栈为空的时候不能用 `pop`。

#### [3. 无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

给定一个字符串 `s` ，请你找出其中不含有重复字符的 **最长子串** 的长度。

解：滑动窗口，这个问题要注意到最长子串的滑动窗口左边递增，右边一定是递增的，不存在左边递增，右边会比原来少的情况，因为你左边递增窗口内字符减少，对右边无重复字符的要求变宽了，右边的空间应该更多才是，所以只需要左右扫描两次就可以了。

#### [21. 合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/)

将两个升序链表合并为一个新的 **升序** 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

解：线性扫描是什么垃圾。这题的模板可以用来解决很多链表两个长度不一而且可能是 `None` 的情形，代码贴贴：

```python
prev = ListNode() # 哨兵防止返回的就是空
now = prev 
while list1 and list2: # 有点牛
  if list1.val < list2.val:
    now.next = list1
    now = now.next
    list1 = list1.next # 注意细节
  else:
    now.next = list2
    now = now.next
    list2 = list2.next
  now.next = list1 if list1 else list2 if list2 else None # 一个扫完了另一个直接挂上
return prev.next # 返回哨兵的下一个
```

#### [26. 删除有序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)

给你一个有序数组 `nums` ，请你**[ 原地](http://baike.baidu.com/item/原地算法)** 删除重复出现的元素，使每个元素 **只出现一次** ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 **[原地 ](https://baike.baidu.com/item/原地算法)修改输入数组** 并在使用 O(1) 额外空间的条件下完成。

解：双指针。

#### [27. 移除元素](https://leetcode-cn.com/problems/remove-element/)

给你一个数组 `nums` 和一个值 `val`，你需要 **[原地](https://baike.baidu.com/item/原地算法)** 移除所有数值等于 `val` 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 `O(1)` 额外空间并 **[原地 ](https://baike.baidu.com/item/原地算法)修改输入数组**。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

解：双指针。

#### [5. 最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/)

给你一个字符串 `s`，找到 `s` 中最长的回文子串。

解：枚举一个或者两个，然后中心拓展。还有一种更简单的 O(n) 算法，懒得看了。

#### [28. 实现 strStr()](https://leetcode-cn.com/problems/implement-strstr/)

给你两个字符串 `haystack` 和 `needle` ，请你在 `haystack` 字符串中找出 `needle` 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  `-1` 。

解：简单题你来 KMP？我直接 find 拜拜了您。注意 index 这个 API 如果找不到会报错。

**KMP 算法**：




