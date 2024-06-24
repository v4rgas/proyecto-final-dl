def move_first_to_last(sentence):
    words = sentence.split()
    if len(words) > 1:
        return ' '.join(words[1:] + words[:1])
    return sentence


def order_words_alphabetically(sentence):
    words = sentence.split()
    return ' '.join(sorted(words))


def reverse_words(sentence):
    words = sentence.split()
    return ' '.join(reversed(words))


def capitalize_first_letter(sentence):
    words = sentence.split()
    return ' '.join(word.capitalize() for word in words)


def replace_spaces_with_hyphens(sentence):
    return sentence.replace(' ', '-')


def remove_vowels(sentence):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in sentence if char not in vowels)


def double_each_word(sentence):
    words = sentence.split()
    return ' '.join(word * 2 for word in words)


def reverse_each_word(sentence):
    words = sentence.split()
    return ' '.join(word[::-1] for word in words)


def add_exclamation_mark(sentence):
    words = sentence.split()
    return ' '.join(word + '!' for word in words)


def to_uppercase(sentence):
    return sentence.upper()


def to_lowercase(sentence):
    return sentence.lower()


def replace_words_with_length(sentence):
    words = sentence.split()
    return ' '.join(str(len(word)) for word in words)


def append_sentence_length(sentence):
    return sentence + ' (' + str(len(sentence.split())) + ' words)'


if __name__ == "__main__":
    test_sentence = "This is an example sentence for testing."

    print(move_first_to_last(test_sentence))
    print(order_words_alphabetically(test_sentence))
    print(reverse_words(test_sentence))
    print(capitalize_first_letter(test_sentence))
    print(replace_spaces_with_hyphens(test_sentence))
    print(remove_vowels(test_sentence))
    print(double_each_word(test_sentence))
    print(reverse_each_word(test_sentence))
    print(add_exclamation_mark(test_sentence))
    print(to_uppercase(test_sentence))
    print(to_lowercase(test_sentence))
    print(replace_words_with_length(test_sentence))
    print(append_sentence_length(test_sentence))
