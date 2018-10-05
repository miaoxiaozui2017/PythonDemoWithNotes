# 回文数
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

><div>
	输入: 121
	输出: true
</div>
示例 2:
><div>
	输入: -121
	输出: false
	解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
</div>

示例 3:
><div>
	输入: 10
	输出: false
	解释: 从右向左读, 为 01 。因此它不是一个回文数。
</div>
>进阶:
	<li>
	你能不将整数转为字符串来解决这个问题吗？
	</li>

```python
# use python3
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x%10 == 0 and x > 0) or (x < 0):
            # 单从整数构成来讲，负整数和10的倍数无论如何也不会是回文数
            return False
        #elif x == 0:
            # （从题目定义上讲0也是回文数）
        #    return True
        else:
            # 从非10倍数的正整数中考虑
            result = 0
            #x_list = []
            tmpx = x
            while tmpx != 0:
                curr = tmpx%10
                tmpx = tmpx//10
                result = result*10 + curr
                #x_list.append(curr)
            #for i in range(len(x_list)//2):
            #    if x_list[i] != x_list[len(x_list)-i-1]:
            #        return False
            #return True
            if result == x:
                return True
            else:
                return False
```
