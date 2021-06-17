# Google STEP Class6 Malloc Challenge

## 問題
First fitで実装された Mallocを、Best fit, Worst fitなどに変更してみて、その比較を行う。

## 比較結果1(メモリ使用率)
| Challenge   | First fit  | Best fit  | Worst fit  |
| ----------- | ----------- | ------------ | ------------ |
| Challenge 1 | 70% | 70% | 70%      |
| Challenge 2 | 40% | 40% | 40%      |
| Challenge 3 | 7% | 50% | 4%      |
| Challenge 4 | 15% | 71% | 7%     |
| Challenge 5 | 15% | 74% | 7%     |

## 比較結果2(実行時間)
| Challenge   | First fit  | Best fit  | Worst fit  |
| ----------- | ----------- | ------------ | ------------ |
| Challenge 1 | 9 ms | 1538 ms | 1675 ms      |
| Challenge 2 | 6 ms | 720 ms | 739 ms      |
| Challenge 3 | 178 ms | 868 ms |  81004 ms     |
| Challenge 4 | 30863 ms | 9269 ms | 820362 ms     |
| Challenge 5 | 23007 ms | 5788 ms | 693168 ms    |

## まとめ
メモリ使用率の面から見ると、Best fitをすると、一番効率よくメモリが使われ、Worst fitは一番メモリ使用率が効率悪くなった。予想通りの結果だと思う。

実行時間の面から見ると、First fitが一番早くて、その次にBest fit。Worst fitが一番遅い結果になった。予想では、First fitが一番早く、Best fitとWorst fitの実行時間はあまり変わらないと思っていたので、少し意外だった。

# Appendix(ターミナルでの実行結果)
## First fit
```
Challenge 1: simple malloc => my malloc
Time: 8 ms => 9 ms
Utilization: 70% => 70%
==================================
Challenge 2: simple malloc => my malloc
Time: 6 ms => 6 ms
Utilization: 40% => 40%
==================================
Challenge 3: simple malloc => my malloc
Time: 159 ms => 178 ms
Utilization: 8% => 7%
==================================
Challenge 4: simple malloc => my malloc
Time: 30144 ms => 30863 ms
Utilization: 15% => 15%
==================================
Challenge 5: simple malloc => my malloc
Time: 21010 ms => 23007 ms
Utilization: 15% => 15%
==================================
```

## Best fit
```
Challenge 1: simple malloc => my malloc
Time: 8 ms => 1538 ms
Utilization: 70% => 70%
==================================
Challenge 2: simple malloc => my malloc
Time: 7 ms => 720 ms
Utilization: 40% => 40%
==================================
Challenge 3: simple malloc => my malloc
Time: 151 ms => 868 ms
Utilization: 8% => 50%
==================================
Challenge 4: simple malloc => my malloc
Time: 30804 ms => 9269 ms
Utilization: 15% => 71%
==================================
Challenge 5: simple malloc => my malloc
Time: 19565 ms => 5788 ms
Utilization: 15% => 74%
==================================
```

## Worst fit
```
Challenge 1: simple malloc => my malloc
Time: 11 ms => 1675 ms
Utilization: 70% => 70%
==================================
Challenge 2: simple malloc => my malloc
Time: 6 ms => 739 ms
Utilization: 40% => 40%
==================================
Challenge 3: simple malloc => my malloc
Time: 138 ms => 81004 ms
Utilization: 8% => 4%
==================================
Challenge 4: simple malloc => my malloc
Time: 18678 ms => 820362 ms
Utilization: 15% => 7%
==================================
Challenge 5: simple malloc => my malloc
Time: 23092 ms => 693168 ms
Utilization: 15% => 7%
==================================
```