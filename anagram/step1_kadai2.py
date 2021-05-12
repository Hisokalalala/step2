from collections import defaultdict, Counter

#scoreの対応表を作る
scorechart = {"a":1, "b":3, "c":2, "d":2, "e":1, "f":3, "g":3, "h":1, "i":1, "j":4, "k":4, "l":2, "m":2, "n":1, "o":1, "p":3, "q":4, "r":1, "s":1, "t":1, "u":2, "v":3, "w":3, "x":4, "y":3, "z":4}

#辞書格納
dict_path = "./words.txt"

with open(dict_path) as f:
    dictionary = [word.strip() for word in f.readlines()]

#重複削除
dictionary = list(set(dictionary))

new_dictionary = defaultdict(int)

for dict_word in dictionary:
    for alphabet in dict_word:
        new_dictionary[dict_word] += scorechart[alphabet]

#スコア順にソートされた辞書(タプル)
sorted_dictionary = sorted(new_dictionary.items(), key=lambda x:x[1], reverse=True)

#条件を満たすスコアが一番高いのを取得

def get_highest(given_word, dictionarys):
    for dict_word in dictionarys:
        given_word_cnt = Counter(given_word)
        dict_word_cnt =  Counter(dict_word[0])
        common = given_word_cnt & dict_word_cnt
        if dict_word_cnt == common:
            return dict_word[0]
    return None


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
