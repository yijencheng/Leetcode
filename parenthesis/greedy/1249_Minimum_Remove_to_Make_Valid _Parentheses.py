Initial thought:
* There is two things we need to handle: extra left & extra right.
* For extra left is simple, use a counter where count++ for '(' and count-- for ')'. If count <0 remove ')'
* For extra left, Maybe is possble to record possible index during the loop(?) 


Solution Idea:
- first time: remove invalid left (but then still may have extra opening bracket)
- second time: looping in reverse order, to remove extra opening bracket
* the idea is, we can remove `any` opening bracket that happens `after` the last balance.
* Say the last zero happen in index=i:
* From 0~i, you cannot remove any one of opening bracket without breaking the total_sum
* From i+1~end, you can remove any of it.
