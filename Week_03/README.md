### **递归**  
递归——循环  
递归和循环没有明显的边界  
#### **特点**  
- 向下进入不同的层；向上又回到原来一层
- 通过参数回到上一层
- 每一层的函数都是一份拷贝，参数传递到不同层  
#### **范型递归代码**
- 递归终结条件  
- 处理当前逻辑  
- 下到下一层  
- 清理当前层  
```
def recursion(level, param1, param2, ...):
    # 递归终结条件
    if level > MAX_LEVEL:
        process_result
        return

    # 处理当前逻辑  
    process(level, data...)

    #下到下一层
    self.recursion(level+1, p1, ...)

    # reverse the current level status if needed
```
#### **「注意」**  
- 不要人肉进行递归（最大的误区）  
- 找到最近最简方法，将其拆解成可重复解决的子问题（重复子问题） 
- 数学归纳法  
### **分治\回溯** 
#### **分治代码**
```
def divide_conquer(problem, param1, param2, ...):
    # 终结条件 recursion terminator
    if problem is None:
        print_result
        return 

    # 处理当前逻辑 prepare data
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)

    #下一层子问题conquer subproblem
    subresult1 = self.divide_conquer(subproblem[0], p1, ...)
    subresult2 = self.divide_conquer(subproblem[1], p1, ...)
    subresult3 = self.divide_conquer(subproblem[2], p1, ...)
    # process and generate the final result
    result = process_result(subresult1, subresult2, subresult3)
    # revert the current level status
```
