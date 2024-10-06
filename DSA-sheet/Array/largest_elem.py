from typing import List


class Solution:
    def largest(self, arr: List[int]) -> int:
        max_num = arr[0]
        for num in arr:
            if num > max_num:
                max_num = num
        return max_num
