"""
Write code that will print out the anagrams (words that use the same letters) from a paragraph of text.
"""

from collections import defaultdict


def anagramsWord(input_paragraph):

    words = list(set(input_paragraph.split()))

    grouped_words = defaultdict(list)
    # Put all anagram words together in a dictionary
    # where key is sorted word
    for word in words:
        grouped_words["".join(sorted(word))].append(word)

    for group in grouped_words.values():
        # if length of group is greater than 1 than anagram words exist
        if len(group) > 1:
            print("Anagram words in the given paragraph are as follows : ")
            print(" ".join(group))


if __name__ == "__main__":
    paragraph = """
    A cat was made to act as if it eats a rat.
    """
    anagramsWord(paragraph)
