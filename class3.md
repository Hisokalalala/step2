# STEP Class2

## 宿題1 モジュール化されたプログラムを「*」「/」に対応させよう
二段階評価をして実装しました。掛け算のトークンを読む関数read_multiplyと割り算のトークンを読む関数read_divideで符号の検知をして、tokenizeを足し算や引き算と同じように書き換えました。そして、tokensを掛け算と割り算を評価するための関数evaluate_multiply_and_divideに渡して一段階目の評価をし、その結果を足し算と引き算を評価するための関数evaluate_plus_and_minusに渡して二段階目の評価をします。

evaluate_multiply_and_divideは引数をtokensとして、返り値を掛け算と割り算だけ評価された新しいtokensとする関数で、evaluate_plus_and_minusは引数をtokensとして返り値を計算結果とする関数です。

関数evaluate_multiply_and_divideから返されたtokensには掛け算と割り算の符号はないので、それをevaluate_plus_and_minusに渡せば、うまく二段階評価が可能になり、計算結果の最終的な答えが返ってくるようになってます。

evaluate_plus_and_minusは元々のevaluateと同じコードです。コードが長くなってきたので、モジュール化のために新しく関数を定義しました。


## 宿題2 書いたプログラムが正しく動いていることを確認するためのテストケースを追加しよう
テストケースは、数字が1つ、2つ、3つの時などを考え、数字の種類が小数か整数かでも場合わけしてなるべく網羅的になるように作りました。また、割り算の時、0で割ることは不可能なので、もし割り算で0がきたらエラーをraiseしています。


## 宿題3 括弧に対応しよう
スタックを使って実装しました。全体のtokenを入れるようのstackと1ペアの括弧の中身を入れて計算する用のminilistというスタックとリストを用意しました。

実装方針としては、閉じ括弧以外のtokenであれば、ひたすらstackに入れて、閉じ括弧が来たときは、stackから順番に取り出し、取り出したものが開き括弧になるまでそれをminilistに要素をリストの先頭から入れていきます。開き括弧が取り出されたら、現在minilistにあるtoken達をevaluate_multiply_and_divideとevaluate_plus_and_minusで二段階評価すると、括弧の中身は計算されたので、計算結果で新しくtokenを作り、それをstackに入れます。tokensの中の全てのtokenが評価された後、stackの中のtoken達に括弧はないので、stackにあるtoken達をevaluate_multiply_and_divideとevaluate_plus_and_minusで二段階評価すると最終的な経験結果が出ます。

テストはいろいろな括弧のパターンを試してみたつもりです。

## まとめ
全体的に、ゴリゴリ実装していくとできたというイメージでした。計算量について最適化を図ってはいないのですが、evaluate_multiply_and_divideでtokenを削除したとき、index=0をして最初から見ていくのではなく、index-=1とすることで、戻り具合を少なくしたりするなどは注意しました。