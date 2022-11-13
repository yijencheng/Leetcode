某一點有多個選擇:

s -> x1 -> a -> b1 -> dst
  -> x2 ->   -> b2


法一：
* [[xxxx]........]
* 0 -> a 可以拆成 0->x1 + 0->x2
* 讓 a approach to len(array)

法二：
* 長方形從右開始，向左逐漸填滿    [........[xxxx]]
* a -> dst 可以拆成 b1->dst + b2->dst
* 讓 a approach to start(0)
