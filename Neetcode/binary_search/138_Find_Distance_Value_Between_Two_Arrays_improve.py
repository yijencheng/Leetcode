#still wrong...
[1,4,2,3]
[-4,-3,6,10,20,30]
3
>> ans: 1(v),2(v),3(x)
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        ans = 0
        
        def larger_than_d(num):
            start, end = 0, len(arr2)-1
            while start<=end:
                mid = (start+end)//2
                d1,d2 =  abs(arr2[mid-1]-num), abs(arr2[mid]-num)
                if min(d1,d2)<d:
                    return False
                elif d1 > d2:
                    start = mid+1
                elif d1 < d2:
                    end = mid-1
            return True
            
        for num in arr1:
            if larger_than_d(num):
                print(num)
                ans+=1
        return ans

#finally....
#key:
# - the minimum dist is the num itself
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        ans = 0
        
        def larger_than_d(num):
            start, end = 0, len(arr2)-1
            while start<=end:
                mid = (start+end)//2
                if abs(arr2[mid]-num)<=d:
                    return False
                elif arr2[mid]<num: #this
                    start = mid+1
                elif arr2[mid]>num: #and this
                    end = mid-1
            return True
            
        for num in arr1:
            if larger_than_d(num):
                ans+=1
        return ans
        
        