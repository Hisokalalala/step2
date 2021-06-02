# Google STEP Class 4 Homework

## 課題内容

### 1. Wikipediaのグラフを使ってなにか面白いことをしてみよう

- 必須："Google"から"渋谷"までを（最短で）たどる方法を探す(幅優先探索)
- "Google"から"渋谷"までを（最短で）たどる方法を探す(ダイクストラでの実装)

ここでは"Google"から”渋谷"までの最短経路が課題であったが、変数を修正すれば他の始点と終点の最短経路も探索できる仕様になっている。

### 2. 他の人の書いたコードを自分の環境で実行してレビューする

- (レビュー後リンクを載せます)

## 準備

[wikipedia_data.zip](https://drive.google.com/file/d/1zqtjSb-ZoR4rzVUWZrjNSES5GKJhYmmH/view?usp=sharing) をダウンロードして解凍し、以下のようなディレクトリ構成にしてください。

```
step_wikipedia-graph
├── data
│   ├── graph_small.png
│   ├── links_small.txt
│   ├── links.txt
│   ├── pages_small.txt
│   └── pages.txt
├── .gitignore
├── README.md
├── wikipedia_sample.cc
├── wikipedia_sample.py
└── WikipediaSample.java
```

## グラフデータ

`data/` に含まれるファイルで、実際に使うものは以下の2つです。

- pages.txt：各ページのidとタイトルのリスト
- links.txt：各リンクのリンク元とリンク先のリスト

以下の3つはテスト用の小さなグラフを表すデータです。

- pages_small.txt
- links_small.txt
- graph_small.png

詳細はスライドを参照してください。

数年前のデータを使っているため、最新の Wikipedia とは異なるリンク構造になっていることに注意してください。


## 実行方法

### Python

テスト環境: Python 3.7.1

#### 課題1-1 "Google"から"渋谷"までを（最短で）たどる方法を探す(幅優先探索)

```shell
python3 wikipedia_sample.py
```
実行時間は、ファイルの読み込みに6分ほど、幅優先探索に2秒です。

また、以下は想定される実行結果の画面です。
```
Google -> セグウェイ -> 渋谷
Shortest distance from Google to 渋谷 is: 2
```

#### 課題1-2 指定された始点から終点までを（最短で）たどる方法を探す(ダイクストラで実装)
```shell
python3 wikipedia_dijkstra.py
```
実行時間は、ファイルの読み込みに6分ほど、ダイクストラに42秒です。

また、以下は想定される実行結果の画面です。
```
Google -> セグウェイ -> 渋谷
Shortest distance from Google to 渋谷 is: 2
```


## コードの実装について

### 課題1-1と1-2共通の関数
#### read_pages
* 引数:file_path(読み込むファイルのパス)
* 返り値:
    * pages_key_is_id(ノードのidがキーで対応するtitleがvalueの辞書)
    * pages_key_is_title(ノードのtitleがキーで対応するidがvalueの辞書)

ノードidとtitleについて記載されているファイルを読み込み、辞書を二つ返す。これにより、idからtitleがわかるし、titleからidがわかるようになる。

#### read_links
* 引数:file_path(読み込むファイルのパス)
* 返り値:links(隣接リスト)

ノード間のリンクについて記載されているファイルを読み込み、リンクの情報を隣接リストに格納して返す。

#### main
* 引数:なし
* 返り値:なし

他の関数たちを組み合わせて、最短経路を調べ、結果を表示するための関数。ここで、変数startとtargetを書き換え、始点と終点を指定できるようになっている。

### 課題1-1
#### bfs
* 引数:
    * pages_key_is_id(ノードのidがキーで対応するtitleがvalueの辞書)
    * pages_key_is_title(ノードのtitleがキーで対応するidがvalueの辞書)
    * links(ノードの隣接リスト)
    * start(始点の名前)
    * target(終点の名前)
* 返り値:
    * 終点が見つかった時に、
        * path[::-1] (最短経路のリスト)
        * shortest_path[target_node] (最短距離)
    * 終点が見つからなかった(始点から終点までのパスが見つからなかった)時に、例外処理として、None, Noneを返すようにしている。

幅優先探索で現在のノードが始点から最短経路になっている時にどのノードから到達したを記録しながら探索していく、そして、最後は終点から前のノードを辿っていくと、経路が見つかる。


### 課題1-2
#### dijkstra
* 引数:
    * pages_key_is_id(ノードのidがキーで対応するtitleがvalueの辞書)
    * pages_key_is_title(ノードのtitleがキーで対応するidがvalueの辞書)
    * links(ノードの隣接リスト)
    * start(始点の名前)
    * target(終点の名前)
* 返り値:
    * 終点が見つかった時に、
        * path[::-1] (最短経路のリスト)
        * shortest_path[target_node] (最短距離)
    * 終点が見つからなかった(始点から終点までのパスが見つからなかった)時に、例外処理として、None, Noneを返すようにしている。

ダイクストラで探索を行うための関数。今回は辺に重みがなかったので、全てを1として計算を行った。もし辺に重みがある場合に対応したいなら、コードのedge_lengthの部分を少し書き換えると対応可能である。


## 実行結果
どちらの方法でも、最短距離2でGoogleから渋谷にたどり着くことができる。ただ、最短経路は一種類だけでないようだ。私が何度かテストしたときは、以下の三つのパスが見つかった。
```
Google -> スターバックス -> 渋谷
Google -> セグウェイ -> 渋谷
Google -> フレッシュアイ -> 渋谷
```