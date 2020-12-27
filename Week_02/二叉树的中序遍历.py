class Solution(object):
    def inorderTraversal(self, root):
        res = []
        def dfs(root):
            if root == None:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res