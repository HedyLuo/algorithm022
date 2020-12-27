"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
"""
extend()用于在列表末尾一次性追加另一个序列中的多个值
list.extend(seq)
"""
class Solution(object):
    def preorder(self, root):
        # 堆栈法
        # if not root:
        #     return []
        # stack, output = [root], []
        # while stack:
        #     root = stack.pop()
        #     output.append(root.val)
        #     stack.extend(root.children[::-1])
        # return output
        # 递归
        res = []
        def dfs(root):
            if not root:
                return
            res.append(root.val)
            if not root.children:
                return
            for child in root.children:
                dfs(child)
        dfs(root)
        return res
