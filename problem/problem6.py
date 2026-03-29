"""
We are building a word processor and we would like to implement a "word-wrap" functionality.
Given a list of words followed by a maximum number of characters in a line, return a collection of strings where each string element represents a line that contains as many words as possible, with the words in each line being concatenated with a single - (representing a space, but easier to see for testing). The length of each string must not exceed the maximum character length per line.
Your function should take in the maximum characters per line and return a data structure representing all lines in the indicated max length.

Examples
pythonwords1 = ["The", "day", "began", "as", "still", "as", "the",
          "night", "abruptly", "lighted", "with", "brilliant", "flame"]

wrapLines(words1, 13)
# => ["The-day-began", "as-still-as", "the-night",
#     "abruptly", "lighted-with", "brilliant", "flame"]

wrapLines(words1, 12)
# => ["The-day", "began-as", "still-as-the", "night",
#     "abruptly", "lighted-with", "brilliant", "flame"]

wrapLines(words1, 20)
# => ["The-day-began-as", "still-as-the-night",
#     "abruptly-lighted", "with-brilliant-flame"]

words2 = ["Hello"]

wrapLines(words2, 5)   # => ["Hello"]
wrapLines(words2, 30)  # => ["Hello"]

words3 = ["Hello", "Hello"]

wrapLines(words3, 5)   # => ["Hello", "Hello"]

words4 = ["Well", "Hello", "world"]

wrapLines(words4, 5)   # => ["Well", "Hello", "world"]

words5 = ["Hello", "HelloWorld", "Hello", "Hello"]

wrapLines(words5, 20)  # => ["Hello-HelloWorld", "Hello-Hello"]

words6 = ["a", "b", "c", "d"]

wrapLines(words6, 20)  # => ["a-b-c-d"]
wrapLines(words6, 4)   # => ["a-b", "c-d"]
wrapLines(words6, 1)   # => ["a", "b", "c", "d"]

All Test Cases
pythonwords1 = ["The","day","began","as","still","as","the","night","abruptly","lighted","with","brilliant","flame"]
words2 = ["Hello"]
words3 = ["Hello", "Hello"]
words4 = ["Well", "Hello", "world"]
words5 = ["Hello", "HelloWorld", "Hello", "Hello"]
words6 = ["a", "b", "c", "d"]

wrapLines(words1, 13)
wrapLines(words1, 12)
wrapLines(words1, 20)
wrapLines(words2, 5)
wrapLines(words2, 30)
wrapLines(words3, 5)
wrapLines(words4, 5)
wrapLines(words5, 20)
wrapLines(words6, 20)
wrapLines(words6, 4)
wrapLines(words6, 1)

"""

words1 = [
    "The",
    "day",
    "began",
    "as",
    "still",
    "as",
    "the",
    "night", 
    "abruptly",
    "lighted",
    "with",
    "brilliant",
    "flame",
]
words2 = ["Hello"]
words3 = ["Hello", "Hello"]
words4 = ["Well", "Hello", "world"]
words5 = ["Hello", "HelloWorld", "Hello", "Hello"]
words6 = ["a", "b", "c", "d"]


def wrapLines(words, max_length):
    result = []
    current_line = ""

    for word in words:
        # case1 - current line is empty put the word directly no dash is needed
        if current_line == "":
            current_line = word
            # print(current_line,word,"case1")
        # case2 - current line already has words
        # check if adding the words with dash still fits
        elif len(current_line) + 1 + len(word) <= max_length:
            current_line = current_line + "-" + word
        # case3 word doesnot fit on current line
        # save current line and start a new one
        else:
            result.append(current_line)
            current_line = word

    # after the loop ends . save the last line

    if current_line != "":
        result.append(current_line)

    return result


print(wrapLines(words1, 13))
# print(wrapLines(words1, 12))
# print(wrapLines(words1, 20))
# print(wrapLines(words2, 5))
# print(wrapLines(words2, 30))
# print(wrapLines(words3, 5))
# print(wrapLines(words4, 5))
# print(wrapLines(words5, 20))
# print(wrapLines(words6, 20))
# print(wrapLines(words6, 4))
# print(wrapLines(words6, 1))
