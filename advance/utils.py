from errno import WSAECONNREFUSED


def char_counter(sentence):
    data = {} # blank dictionary
    for char in set(sentence):
        print(char, sentence.count(char))
        data[char] = sentence.count(char)
    return data 
def word_counter(sentence):
    data = {} # blank dictionary
    words = sentence.split()
    for word in set(words):
        data[word] = words.count(word)
    return data 
def remove_punc(sentence):
    '''remove punctuation ( to be coded {tbc})''' 
    pass 