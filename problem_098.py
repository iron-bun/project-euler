#!/usr/bin/env python3

#By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 362. What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 962. We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted, neither may a different letter have the same digital value as another letter.
#
#Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).
#
#What is the largest square number formed by any member of such a pair?
#
#NOTE: All anagrams formed must be contained in the given text file.

import itertools

def get_strings(word_list):
    for word in word_list:
        if len(word) == 1:
            continue
        word_letters = sorted(word)
        tmp = (word, list(v for v in word_list if word != v and word != v[::-1] and sorted(v) == word_letters))
        if len(tmp[1]) == 0:
            continue
        yield tmp

def get_word_value(word, mapping):
    if mapping[word[0]] == '0':
        return 2
    else:
        return int("".join(map(lambda x: mapping[x], list(word))))

square_cache = {}
def find_squares(word, anagrams, minimum):
    word_key = "".join(sorted(word))
    check_cache = square_cache.get(word_key, None)
    if check_cache:
        yield check_cache
        return
    square_cache[word_key] = 1

    letters = set(word)
    for permutation in itertools.permutations(list("9876543210"), len(letters)):
        mapping = {letter: value for letter, value in zip(letters, permutation)}

        word_value = get_word_value(word, mapping)
        if word_value <= minimum:
            continue

        elif int(word_value**0.5) == word_value**0.5:
            for tmp in [get_word_value(v, mapping) for v in anagrams]:
                if int(tmp**0.5) == tmp**0.5 and max(word_value,tmp) > square_cache[word_key]:
                    square_cache[word_key] = max(word_value, tmp)
                    minimum = max(word_value, tmp)
                    yield word_value

with open('data/p098_words.txt') as f:
    word_list = f.read().split(",")
    word_list = [v.strip("\"") for v in word_list]
    word_list = sorted(word_list, key=len, reverse = True)
    generator = get_strings(word_list)

ans = 0
for word_set in generator:
    print(word_set)
    for tmp in find_squares(*word_set, ans):
        if tmp > ans:
            ans = tmp

print(ans)
