Tags
Dict
#tag:duplicate
#tag:frequency

Array





# 先還是後?
### sliding window 的先後
p219
```
    for i in range(len(nums)):
        if nums[i] in s:
            return True
        
        ## ====== fix-length window 
        s.add(nums[i])
        if len(s) == k+1:
            s.remove(nums[i-k])
        ## ====== end
    return False 
```
在p424中有這段代碼
```
    for r in range(len(s)):
        ##########
        d[s[r]] = d.get(s[r],0)+1
        while (r-l+1) - max(d.values()) > k:
            d[s[l]]-=1
            l+=1
        #######
        longest = max(longest, r-l+1)

    return longest
```

### 遞迴的先後





### Stack
* 跟Array搭配，記住Index (p.1249)

### While loop
* 停在符合條件的index vs 停在第一個不符合的index
i = 0
while i<len(arr) and condition:
    i+=1

i = 0
while i<len(arr):
    if !condition:
        break
    i+=1
