from collections import Counter

import re

import constants

def clean_words(words, min_length=0, max_length=999) -> list:
    """
        Removes punctuation and special characters from words of specified length

        :param words: List of words
        :param min_length: Minimal length of a word
        :param max_length: Maximal length of a word

        :return: List of words without punctuation and special characters
        :rtype: list
    """
    for i in range(len(words)):
        words[i] = re.sub(r"[^А-Яа-яЁё\s]", "", words[i])

    words = [word.lower().strip() for word in words if min_length <= len(word.lower().strip()) <= max_length]

    return words

def extract_filler_words(data) -> set:
    """
        Extracts filler words from given data

        :param data: Data with filler words marked as <filler_words>...</filler_words>

        :return: Set of filler words
        :rtype: set
    """
    filler_lists = data["text"].str.findall(r"<filler_words>(.*?)</filler_words>")

    filler_lists = filler_lists.apply(lambda text: clean_words(text, constants.filler_word_len_min, constants.filler_word_len_max))

    filler_words = []

    for filler_list in filler_lists:
        for word in filler_list:
            filler_words.append(word)

    words_freq = Counter(filler_words)

    filler_words = [word for word in filler_words if words_freq[word] >= constants.filler_word_threshold]

    filler_words = set(filler_words)

    return filler_words