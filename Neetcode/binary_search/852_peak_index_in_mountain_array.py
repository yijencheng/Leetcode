#correct, but not good.
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start, end = 0, len(arr)-1
        while start<=end:
            mid = (start+end)//2
            if (mid == 0 or arr[mid-1] < arr[mid]) and (mid == len(arr)-1 or arr[mid] > arr[mid+1]):
                return mid
            elif mid == 0 or arr[mid-1] < arr[mid]:
                start = mid+1
            elif mid == len(arr)-1 or arr[mid-1] > arr[mid]:
                end = mid-1

#suggested solution
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start, end = 1, len(arr)-2
        while start<=end:
            mid = (start+end)//2
            if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid-1] < arr[mid]:
                start = mid+1
            elif arr[mid-1] > arr[mid]:
                end = mid-1
