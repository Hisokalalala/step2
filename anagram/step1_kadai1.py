from collections import defaultdict

#辞書格納
path = "./words.txt"

with open(path) as f:
    dictionary = [word.strip() for word in f.readlines()]

d = defaultdict(list)

#新しい辞書作り
for i in range(len(dictionary)):
    temp = "".join(sorted(dictionary[i]))
    d[temp].append(dictionary[i])

new_dictionary = dict(d)

#辞書のソート
sorted_key = sorted(new_dictionary.keys())

#二分探索
def binary_search(target, dataset, dictionaryset):
    start = 0
    end = len(dataset) - 1
    while start <= end:
        mid = (start + end) // 2
        if dataset[mid] == target:
            return dictionaryset[target]
        elif dataset[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

#最終的な方法
def better_solution(random_word, keyset, dictionaryset):
    sorted_random_word = "".join(sorted(random_word))

    anagram = binary_search(sorted_random_word, sorted_key, new_dictionary)
    if anagram != None:
        return anagram
    else:
        return "Not FOUND"

#print(better_solution("udb", sorted_key, new_dictionary))