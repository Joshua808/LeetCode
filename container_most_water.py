from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while right != left:
            max_area = max(min(height[right], height[left]) * (right-left), max_area)

            if height[right] > height[left]:
                left +=1
            else:
                right -=1



        print(max_area)
        return max_area



leetcode = Solution()
leetcode.maxArea([1,8,6,2,5,4,8,3,7])



