def count_characters(text):
    characters = len(text)
    print("Characters:", characters)

def count_words(text):
    words = len(text.split())
    print("Words:", words)

def find_longest_word(text):
    text = text.split()
    large = 0
    longest_word = ""
    for word in text:
        if len(word) > large:
            large = len(word)
            longest_word = word
    print("Longest Word", longest_word)

def find_common_character(text):
    my_dict = {}
    for c in text:
        if c == " ":
            continue
        if c not in my_dict:
            my_dict[c] = 1
        else:
            my_dict[c] +=1

    large = 0
    most_common_character = ""
    for el in my_dict:
        if my_dict[el] > large:
            large = my_dict[el]
            most_common_character = el
    print("Most Common Character:", most_common_character)

def find_number_of_vowels(text):
    vowels = ['a','e','i','o','u']
    vowel_count = 0
    for el in text:
        if el in vowels:
            vowel_count += 1
    print("Number of Vowels", vowel_count)

def find_number_of_unique_words(text):
    unique_words = []
    text = text.split()
    for word in text:
        if word not in unique_words:
            unique_words.append(word)

    count_unique_words = len(unique_words)
    print("Number of Unique Words:", count_unique_words)



text = input("Enter your text:")
count_characters(text)
count_words(text)
find_longest_word(text)
find_common_character(text)
find_number_of_vowels(text)
find_number_of_unique_words(text)