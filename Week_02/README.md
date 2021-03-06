#### 哈希表、映射、集合
哈希表对应python中的字典，以键值对的形式存储数据；  
集合对应set()、HashSet()，数据不重复；  
应用：用户表、电话号码表、键值对存储（redis）  

#### 树、二叉树、二叉搜索树
树的示例
```
    class TreeNode:  
        def __init__(self,val):
            self.val = val  
            self.left, self.right = Node, Node​​​
```

树的遍历  
- 前序：跟节点再左子树，后右子树；中  左 右  
- 中序：先叶子后节点，左 中 右  
- 后序：先叶子后节点，左 右 中  
- 层序遍历：从左到右一层一层访问  

二叉搜索树：指一棵空树或者具有下列性质的二叉树  
- 左子树的所有节点的值均小于它的根节点的值  
- 右子树的所有节点的值均大于它的根节点的值  
- 以次类推：左右紫薯也分别为二叉搜索树（重复性）

二叉搜索树的升序排序是中序遍历，插入、查询的复杂度logn  

堆、二叉堆  
- heap：可以迅速找到一堆数中的最大或者最小值的数据结构，抽象的数据结构  
- 堆的实现有多种，并不独指二叉堆（常见且简单，但不是最优解）  
- 堆的插入：插入到底部，再依次向上层移动，时间复杂度logn  
- 堆的删除：删除的元素被最后一个叶子节点替代，叶子节点再向下层寻找合适的位置  

图的常见算法：DFS（深度优先）、BFS（广度优先）