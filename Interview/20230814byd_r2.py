# encoding: utf-8
# a = input("please input a number:")
print("hello world")

# 1,2,5,6,7,10

#  x     1
# x 2    x 2


def findSumEqual(arr, target):
    arr = sorted(arr)
    ans = []
    cur = []
    def dfs(i, target):
        if i == len(arr):
            if target == 0:
                ans.append(cur.copy())
            return
        if target==0:
            ans.append(cur.copy())
            return
        elif target <0:
            return
        # pick
        cur.append(arr[i])
        dfs(i+1, target-arr[i])
        cur.pop()

        # not pick
        dfs(i+1, target)

    dfs(0, target)
    return ans


test1 = [10,1,2,7,6,5]
print(findSumEqual(test1, 8))

