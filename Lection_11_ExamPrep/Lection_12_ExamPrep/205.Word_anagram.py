try:
    words_fn = input()
    word_anagram = input()
    word_to_check = sorted(word_anagram)

    anagrams =[]
    with open(words_fn, encoding='utf-8') as f:
        for line in f:
            word = line.strip()
            if word != word_anagram and word_to_check == sorted(word):
                anagrams.append(word)

    if anagrams:
        anagrams.sort()
        for word in anagrams:
            print(word)
    else:
        print("NO ANAGRAMS")

except:
    print("INVALID INPUT")
