"""
We are playing a word game in which one player starts with a word, and then the next player tries to construct a word using all of the letters from the first word except one. For example:

If we start with the word "DEVOTE", we could make "VOTED". This uses all the letters except one "E".
We cannot use letters more often than they appear in the original word. For example, we can turn "EXPANSE" into "APEXES" since there were 2 Es in EXPANSE. However, you cannot turn "FROWN" into "WOOF", since FROWN only has one O.
You must use all but one of the letters. For example, "WOWS" cannot turn into "OW".

We would like to figure out if a list of words representing a game is valid. For example:

words_1 = ["DEVOTE", "VOTED", "DOTE", "DOT", "TO"]
words_2 = ["FROWN", "GOWN", "WON", "NO"]

Our function would return True for words_1: This represents a valid sequence of words. However, words_2 would return False, since FROWN cannot lead to GOWN.

Write a function that takes in a list of strings and determines if they represent a valid sequence of words.

Other examples:

words_1  = ["DEVOTE", "VOTED", "DOTE", "DOT", "TO"]
words_2  = ["FROWN", "GOWN", "WON", "NO"]
words_3  = ["FROWN", "WOOF", "FOO", "OF"]
words_4  = ["WOWS", "WOW", "OW"]
words_5  = ["VOWS", "WOWS", "WOW", "OW"]
words_6  = ["WOWS", "OW"]
words_7  = ["EXPANSE", "APEXES", "PEACE", "PACE", "PAC", "PA"]
words_8  = ["CATALOGS", "GELATOS", "GELATO", "GLOAT", "TOGA", "OAT", "TO"]
words_9  = ["RAINOUTS", "RAINOUT", "AROINT", "TRAIN", "ANTI", "NIT", "IT"]
words_10 = ["CROOKEST", "ROCKETS", "SECTOR", "TORES", "TOSE", "EST", "ST"]
words_11 = ["CROOKEST", "ROCKETS", "SOCKET", "STOKE", "SOCK", "KOS", "SO"]
words_12 = ["CROOKEST", "ROCKETS", "SECTOR", "SCORE", "CORE", "ORE", "SO"]

"""
words_1  = ["DEVOTE", "VOTED", "DOTE", "DOT", "TO"]
words_2  = ["FROWN", "GOWN", "WON", "NO"]
words_3  = ["FROWN", "WOOF", "FOO", "OF"]
words_4  = ["WOWS", "WOW", "OW"]
words_5  = ["VOWS", "WOWS", "WOW", "OW"]
words_6  = ["WOWS", "OW"]
words_7  = ["EXPANSE", "APEXES", "PEACE", "PACE", "PAC", "PA"]
words_8  = ["CATALOGS", "GELATOS", "GELATO", "GLOAT", "TOGA", "OAT", "TO"]
words_9  = ["RAINOUTS", "RAINOUT", "AROINT", "TRAIN", "ANTI", "NIT", "IT"]
words_10 = ["CROOKEST", "ROCKETS", "SECTOR", "TORES", "TOSE", "EST", "ST"]
words_11 = ["CROOKEST", "ROCKETS", "SOCKET", "STOKE", "SOCK", "KOS", "SO"]
words_12 = ["CROOKEST", "ROCKETS", "SECTOR", "SCORE", "CORE", "ORE", "SO"]

def valid_words(words):
    for i in range(1,len(words)):
        if(len(words[i]) != (len(words[i-1])-1)):
            return False
        
        ch_freq = {}

        for ch in words[i-1]:
            ch_freq[ch] = ch_freq.get(ch,0) + 1
        
        for ch in words[i]:
            if ch_freq.get(ch,0) == 0:
                return False
            
            ch_freq[ch] -= 1
        
    return True

print(valid_words(words_2))