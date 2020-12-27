"""
题目链接：https://leetcode-cn.com/problems/valid-anagram/
思路：
1，判断长度，长度不同输出false
2.对字母排序，并对比
->也可以直接对比
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = ''.join(sorted(list(s)))
        b = ''.join(sorted(list(t)))
        return a == b


"""
法二：将s/t分别存入字典，key存字符，value为统计字符出现的字符，再比较字典
「学习函数」dict.get(key,default=None)，key--字典中要查找的键值，default--如果指定的键值不存在则返回默认值
"""
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        ds = {}
        dt = {}
        for i in s:
            ds[i] = ds.get(i, 0) + 1
        for j in t:
            dt[j] = dt.get(j, 0) + 1
        return ds == dt
