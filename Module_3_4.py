def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.upper().count(i.upper()) > 0 or i.upper().count(root_word.upper()) > 0:
            same_words.append(i)

    return same_words


print(*single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(*single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
