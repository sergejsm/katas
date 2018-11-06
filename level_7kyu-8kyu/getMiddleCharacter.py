def get_mdiddle_character(word):
    wordLength = len(word)
    if wordLength%2 == 0 :
        return (word[wordLength//2 - 1] + word[wordLength//2])
    else:
        return (word[wordLength//2])
