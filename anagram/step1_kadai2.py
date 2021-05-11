from collections import defaultdict, Counter

#scoreの対応表を作る
scorechart = {"a":1, "b":3, "c":2, "d":2, "e":1, "f":3, "g":3, "h":1, "i":1, "j":4, "k":4, "l":2, "m":2, "n":1, "o":1, "p":3, "q":4, "r":1, "s":1, "t":1, "u":2, "v":3, "w":3, "x":4, "y":3, "z":4}

#辞書格納
dict_path = "./words.txt"

with open(dict_path) as f:
    dictionary = [word.strip() for word in f.readlines()]

#重複削除
dictionary = list(set(dictionary))

d = defaultdict(int)

for i in range(len(dictionary)):
    temp = dictionary[i]
    for j in range(len(temp)):
        d[temp] += scorechart[temp[j]]

new_dictionary = dict(d)

#スコア順にソートされた辞書
sorted_dictionary = sorted(new_dictionary.items(), key=lambda x:x[1], reverse=True)

#条件を満たすスコアが一番高いのを取得
def get_highest(given_word, dictionary_dataset):
    for i in range(len(dictionary_dataset)):
        common = sorted(list((Counter(given_word) & Counter(dictionary_dataset[i][0])).elements()))
        temp = sorted(dictionary_dataset[i][0])
        if temp == common:
            return dictionary_dataset[i][0]
    return None

"""
上記の辞書の単語がgiven_wordに含まれているかの比較方法はもう少し賢い方法がありそう
"""

#パス指定
input_path = "./medium.txt"
output_path = "./medium_answer.txt"

with open(input_path) as f:
    inputs = [word.strip() for word in f.readlines()]
with open(output_path, mode="w") as f:
    for i in range(len(inputs)):
        temp = get_highest(inputs[i], sorted_dictionary)
        f.write(temp)
        f.write("\n")

print("Finished!")
