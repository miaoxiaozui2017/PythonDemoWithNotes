# 移动零

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

><div>
    输入: [0,1,0,3,12]
    输出: [1,3,12,0,0]
</div>

>说明:
    <ol>
        1.必须在原数组上操作，不能拷贝额外的数组。
    </ol>
    <ol>
        2.尽量减少操作次数。
    </ol>

```python
# use python3
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        count0 = 0
        while i < len(nums):
            if nums[i] == 0:
                del nums[i]
                count0 = count0 + 1
            else:
                i = i + 1
        for i in range(count0):
            nums.append(0)
        pass
```
