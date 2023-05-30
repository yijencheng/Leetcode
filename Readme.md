# General guide

### Stack
* 跟Array搭配，記住Index (p.1249)

### While loop
* 停在符合條件的index vs 停在第一個不符合的index
i = 0
while i<len(arr) and condition:
    i+=1

i = 0
while i<len(arr):
    if !{n+1 condition}:
        break
    i+=1
