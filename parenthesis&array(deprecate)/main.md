Sol1: left_min, left_max method
# update left_min, left_max
# check (noted the order is important)
# - left_max <0, failed
# - left_min <0, increase (chanfe)


Sol2: two pass
* first, only change ')' to '(' when count <0
* second pass, change '(' to `)