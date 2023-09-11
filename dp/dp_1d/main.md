某一點有多個選擇:

s --> x1 -> i -> b1 --> dst
  --> x2 -> i -> b2 -->


法一(l2r)
* [[xxxx]........]
* [0, i] 可以拆成 operator([0, x1] + x1->i, [0, x2] + x2->i, [0, x3] + x3->i)
* 讓 i approach to len(array)

法二(r2l)
* 長方形從右開始，向左逐漸填滿    [........[xxxx]]
* [i, dst] 可以拆成 b1->dst + b2->dst
* 讓 a approach to start(0)
