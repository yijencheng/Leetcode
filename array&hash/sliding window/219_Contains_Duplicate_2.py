Given an integer array nums and an integer k, 
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        for i in range(len(nums)):
            if nums[i] in s:
                return True
            
            ## ====== fix-length window 
            s.add(nums[i])
            if len(s) == k+1:
                s.remove(nums[i-k])
            ## ====== end
        return False 
                

                
                
        
                
        