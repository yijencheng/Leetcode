Step1. Define DFS argument
1. where am I
2. what are the things need to check condition-match?

### Where am I
2d array: i,j





Step2. Define DFS
1. Is this place valid?
2. Do I need to continue? (condition)
    * if not, early return
    * if match, any thing to do?
3. what's next? How to traverse?


For the above, 3 & 1 is connectet. The way you traverse will affect whether you're possible to enter invlid position or not
### Is this place valid



* out of bound + revisit
* current booard[i][j] != {match condition}
* end condition