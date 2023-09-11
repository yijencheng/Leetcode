#my
- find maximum element's index
- two problems: [left, max item], [max item, right]
- for each problem, continue to sum over left_min ~ cur 

>>> concern: the center is not quite easy to find, and may have multiple largest element 

to add on previous idea, we can compare left with right
- for each point, 上面可以積的水 = min(left_max, right_max)

#better and correct
class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        l_max, r_max = height[l],height[r]
        ans = 0
        while l<r:
            if l_max < r_max:
                l+=1
                if l_max < height[l] or r_max < height[l]:
                    l_max = max(l_max, height[l])
                else: #should contain water
                    ans  += l_max - height[l]
                    l_max = max(l_max, height[l])
            else:
                r-=1
                if l_max < height[r] or r_max < height[r]:
                    r_max = max(r_max, height[r])
                else:
                    ans  += r_max - height[r]
                    r_max = max(r_max, height[r])
            
        return ans

#wrong
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        for i in range(1, len(height)-1):
            left_max, right_max = max(height[:i]), max(height[i+1:])
            ans += min( left_max,  right_max) - height[i]
        return ans

#correct, but TLE (O(n^2))
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        for i in range(1, len(height)-1):
            cur = height[i]
            left_max, right_max = max(height[:i]), max(height[i+1:])
            
            if left_max < cur or right_max < cur:
                continue
            else:
                ans += min( left_max,  right_max) - cur
        return ans


# optimized to linear 
class Solution:
    def trap(self, height: List[int]) -> int:
        left_max, right_max = [0]*len(height), [0]*len(height)
        ans = 0
    
        cur_max = 0
        for i,h in enumerate(height):
            left_max[i] = cur_max
            cur_max = max(cur_max, h)
        cur_max = 0
        for i in range(len(height)-1, -1,-1):
            right_max[i] = cur_max
            cur_max = max(cur_max, height[i])
        
        
        for i in range(1, len(height)-1):
            cur = height[i]
            if left_max[i] < cur or  right_max[i] < cur:
                continue
            else:
                ans += min( left_max[i],  right_max[i]) - cur
            
        return ans

#optimized to constant memory
class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        l_max, r_max = height[l],height[r] <<<< be careful!!!
        ans = 0
        while l<r:
            if l_max < r_max:
                l+=1
                if l_max < height[l] or r_max < height[l]:
                    l_max = max(l_max, height[l])
                    continue
                else:
                    ans  += min(l_max, r_max) - height[l]
                    l_max = max(l_max, height[l])
            else:
                r-=1
                if l_max < height[r] or r_max < height[r]:
                    r_max = max(r_max, height[r])
                    continue
                else:
                    ans  += min(l_max, r_max) - height[r]
                    r_max = max(r_max, height[r])
            
        return ans