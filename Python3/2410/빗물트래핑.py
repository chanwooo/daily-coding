from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height)-1
        l_max, r_max = height[left], height[right]

        while left < right:
            print(left, l_max, height[left],"|", right, r_max,height[right],"|", volume)
            l_max, r_max = max(height[left], l_max), max(height[right], r_max)

            if l_max <= r_max:
                volume += l_max - height[left]
                left +=1
            else:
                volume += r_max - height[right]
                right -=1

        return volume



print("ans: ",Solution.trap(Solution,[0,1,0,2,1,0,1,3,2,1,2,1]))