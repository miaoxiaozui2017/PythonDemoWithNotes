# 反转整数

给定一个 32 位有符号整数，将整数中的数字进行反转。

>注意:
    <li>
        假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
    </li>

示例 1:

><div>
	输入: 123
	输出: 321
</div>
示例 2:

><div>
	输入: -123
	输出: -321
</div>
示例 3:

><div>
	输入: 120
	输出: 21
</div>
```python
# use python3
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        mark = 1
        if x < 0:
            mark = -1
            x = -x
        result = 0 
        while x != 0:
            curr = x%10
            x = x//10
            result = result*10+curr
        if (-2**31<= result*mark <= 2**31-1):
            return result*mark
        else:
            return 0
```
