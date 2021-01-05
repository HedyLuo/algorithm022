### **深度优先搜索/广度优先搜索**
搜索-遍历  
- 每个节点都要访问一次  
- 每个节点仅访问一次  
- 节点搜索顺序不同，即深度、广度  
#### **树结构** 
```
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, Node
```
**深度优先**
```
def dfs(node):
    if node in visited:
        # already visited
        return
    visited.add(node)   # visited.append(node)

    # process current node 
    # ... # logic here
    dfs(node.left)
    dfs(node.right)
```
```
# 递归写法
visited = set()
def dfs(node, visited):
    if node in visited:
        # already visited
        return
    visited.add(node)
    # process current node here
    ...
    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node, visited)
```
```
# 堆栈写法
def dfs(self, tree):
    if tree.root is None:
        return []
    visited, stack = [], [treee.root]
    while stack:
        node = stack.pop()
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        stack.push(nodes)
    ...
```
**广度优先**
```
# 队列写法
def bfs(graph, start, end):
    queue = []
    queue.append([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)
    ...
```
### **贪心算法Greedy**
贪心算法：在每一种或每一步的情况下选择最优解，不能回退；局部做最优判断  
动态规划：会保存以前的运算结果，并根据之前的结果进行选择，有回退功能；全局判断+回退  
回溯：能够回退  
贪心算法使用场景：求图的最小生成树、哈夫编码；对于工程和生活中的问题，贪心算法并不能得到我们想要的答案
### **二分查找**
使用二分查找的前提：  
- 目标函数单调性（递增或递减），即有序  
- 存在上下界  
- 能够通过索引访问
```
left, right = 0, len(array)-1
while left <= right:
    mid = (leff+right)/2
    if array[mid] == target:
        return result or break
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid -1 
```