# Problem: [1,2,3,4]


num = [1,2,3,4]
def func1(nums):
    cum = 0
    ans = [0]*len(nums)
    for i in range(len(nums)):
        cum+=nums[i]
        ans[i] = cum
    print(ans) # [1, 3, 6, 10]

func1(num)


def func2(nums):
    cum = 0
    ans = [0]*len(nums)
    for i in range(len(nums)):
        ans[i] = cum
        cum+=nums[i]
    print(ans) # [0, 1, 3, 6]

func2(num)


num = [1,-2,-5,8,2]
def func3(nums):
    cum = 0
    ans = [0]*len(nums)
    for i in range(len(nums)):
        if cum <0:
            cum = 0
        cum+=nums[i]
        ans[i] = cum
    print(ans) # [1, -1, -5, 8, 10]

func3(num)

def func4(nums):
    cum = 0
    ans = [0]*len(nums)
    for i in range(len(nums)):
        cum+=nums[i]
        if cum <0:
            cum = 0
        ans[i] = cum
    print(ans) # [1, 0, 0, 8, 10]

func4(num)
