from collections import Counter

import re

import constants

def clean_filler_words(filler_words) -> list:
    """
        Removes punctuation and special characters from filler words of specified length

        :param filler_words: List of potential filler words

        :return: List of filler words without punctuation and special characters
        :rtype: list
    """
    for i in range(len(filler_words)):
        filler_words[i] = re.sub(r"[^А-Яа-яЁё\s]", "", filler_words[i])

    filler_words = [word.lower().strip() for word in filler_words if constants.filler_word_len_min <= len(word.lower().strip()) <= constants.filler_word_len_max]

    return filler_words

def extract_filler_words(data) -> set:
    """
        Extracts filler words from given data

        :param data: Data with filler words marked as <filler_words>...</filler_words>

        :return: Set of filler words
        :rtype: set
    """
    filler_lists = data["text"].str.findall(r"<filler_words>(.*?)</filler_words>")

    filler_lists = filler_lists.apply(clean_filler_words)

    filler_words = []

    for filler_list in filler_lists:
        for word in filler_list:
            filler_words.append(word)

    words_freq = Counter(filler_words)

    filler_words = [word for word in filler_words if words_freq[word] >= constants.filler_word_threshold]

    filler_words = set(filler_words)

    return filler_words