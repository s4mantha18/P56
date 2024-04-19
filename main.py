def count_words(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

print(count_words("hello world hello"))  # Output: {'hello': 2, 'world': 1}
