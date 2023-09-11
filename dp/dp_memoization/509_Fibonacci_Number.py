# without mem
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:return 0
        if n == 1:return 1
        return self.fib(n-1)+self.fib(n-2)
    

# with mem
class Solution:
    def fib(self, n: int) -> int:
        mem = {}
        if n == 0:return 0
        if n == 1:return 1
        
        if n in mem: return mem[n]
        mem[n] = self.fib(n-1) + self.fib(n-2)
            
        return mem[n]


# =========   BAD  ============ 
#  class Solution:
#     def fib(self, n: int) -> int:
#         mem = {}
#         if n == 0:return 0
#         if n == 1:return 1
        
#         if n-2 in mem: 
#             prev_2 = mem[n-2]
#         else:
#             prev_2 = self.fib(n-2)
#             mem[n-2] = prev_2
        
#         if n-1 in mem: 
#             prev_1 = mem[n-1]
#         else:
#             prev_1 = self.fib(n-1)
#             mem[n-1] = prev_1
            
#         return prev_2+prev_1



# class Solution:
#     def fib(self, n: int) -> int:
#         mem = {}
#         if n == 0:return 0
#         if n == 1:return 1
        
#         if n-1 not in mem: mem[n-1] = self.fib(n-1)
#         if n-2 not in mem: mem[n-2] = self.fib(n-2)
            
#         return mem[n-1]+mem[n-2]