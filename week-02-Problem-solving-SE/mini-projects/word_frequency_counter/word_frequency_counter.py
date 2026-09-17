def word_frequency_counter(text):
    word_count = {}
    text = text.split()
    for word in text:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    for word in word_count:
        print(f"{word} : {word_count[word]}")


text = input("Enter your text:")
word_frequency_counter(text)