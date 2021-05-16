from collections import defaultdict, OrderedDict

#辞書格納
path = "./words.txt"

with open(path) as f:
    dictionary = [word.strip() for word in f.readlines()]

new_dictionary = defaultdict(list)

#新しい辞書作り
for dict_word in dictionary:
    sorted_word = "".join(sorted(dict_word))
    new_dictionary[sorted_word].append(dict_word)

#辞書のソート
sorted_key = sorted(new_dictionary.keys())

#二分探索
def binary_search(target, sorted_keys, dictionary):
    start = 0
    end = len(sorted_keys) - 1
    while start <= end:
        mid = (start + end) // 2
        if sorted_keys[mid] == target:
            return dictionary[target]
        elif sorted_keys[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

def binary_search2(target, order_dictionary):
    start = 0
    end = len(order_dictionary) - 1
    while start <= end:
        mid = (start + end) // 2
        if order_dictionary.key_at(mid) == target:
            return order_dictionary.value_at(mid)
        elif order_dictionary.key_at(mid) < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

#最終的な方法
def better_solution(random_word, sorted_keys, dictionary):
    sorted_random_word = "".join(sorted(random_word))

    anagram = binary_search(sorted_random_word, sorted_keys, new_dictionary)
    if anagram != None:
        return anagram
    else:
        return "Not FOUND"

print(better_solution("udb", sorted_key, new_dictionary))


"""
#応用問題

from collections import OrderedDict

ordered_dictionary = OrderedDict(sorted(new_dictionary.items(), key=lambda x:x[0]))

def binary_search2(target, order_dictionary):
    sorted_keys = list(order_dictionary.keys())
    start = 0
    end = len(sorted_keys) - 1
    while start <= end:
        mid = (start + end) // 2
        if sorted_keys[mid] == target:
            return order_dictionary[target]
        elif sorted_keys[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

def better_solution2(random_word, dictionary):
    sorted_random_word = "".join(sorted(random_word))

    anagram = binary_search2(sorted_random_word, dictionary)
    if anagram != None:
        return anagram
    else:
        return "Not FOUND"

print(better_solution2("udb", ordered_dictionary))
"""


