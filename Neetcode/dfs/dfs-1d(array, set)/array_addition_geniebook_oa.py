# Problem: return True if any combination of number can be added up to the largest number in the array

# Ex1. [5,7,16,1,2]
# Output: False
# Ex2. [3,5,-1,8,12]
# Output: True

# my answer at the time (wrong)
def sol(arr):
    target = max(arr)
    arr = sorted(arr)
    found = [False]

    def dfs(cur, i):
        if i == len(arr):
            return 
        if sum(cur) == target:
            found[0] = True
            return
        dfs(cur, i+1)
        # wrong part
        if i < len(arr)-1 and sum(cur) + arr[i+1] <=target and arr[i+1] > 0:
            dfs(cur+[arr[i+1]], i+1)
    
    dfs([],0)
    return found[0]

    
# sol
def sol_2(arr):
    target = max(arr)
    arr = sorted(arr)
    found = [False]

    def dfs(cur, i):
        if i == len(arr):
            return 
        if sum(cur) == target:
            found[0] = True
            return
        dfs(cur, i+1)
        # wrong part
        if sum(cur) + arr[i] <=target:
            dfs(cur+[arr[i]], i+1)
    
    dfs([],0)
    return found[0]

print( sol_2([5,7,16,1,2]) ) # False
print( sol_2([3,5,-1,8,12]) ) # True

