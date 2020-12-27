"""
自己能想到的做法：暴力求解，时间复杂度为O(N^2）
题解思路：
1。查找target-nums[i]是否在i的前半部分中，如果在，返回下标
2。有点疑惑为什么他还需要判断j的大小，自己试了一下不判断j也可以..不知道这样会带来什么后果???
"""
class Solution(object):
    def twoSum(self, nums, target):
        # j = -1
        for i in range(len(nums)):
            if target - nums[i] in nums[:i]:
                j = nums.index(target-nums[i])
                break
        # if j >= 0:
        #     return [j, i]
        return [j, i]