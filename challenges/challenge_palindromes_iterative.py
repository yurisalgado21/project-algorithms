def is_palindrome_iterative(word):
    word_backwards = word[::-1]
    if len(word) == 0:
        return False
    if word_backwards == word:
        return True
    if word_backwards != word:
        return False
