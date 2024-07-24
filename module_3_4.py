def single_root_words(root_word, *other_words):
    same_words = []
    for x in other_words:
        x1 = x.lower()
        s1 = root_word.lower()
        if x1 in s1 or s1 in x1:
            same_words.append(x)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
