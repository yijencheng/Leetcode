 #wrong!!!
 def isPalindrome(self, x: int) -> bool:
        if x<0:return False
        
        x = str(x)
        i,j = 0, len(x)-1
        
        
        while i!=j:
            if x[i]!=x[j]:return False
            i+=1
            j-=1
        return True

#correct
 def isPalindrome(self, x: int) -> bool:
        if x<0:return False
        
        x = str(x)
        i,j = 0, len(x)-1
        
        
        while i<j:
            if x[i]!=x[j]:return False
            i+=1
            j-=1
        return True
