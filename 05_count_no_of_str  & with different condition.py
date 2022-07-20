def match_words(words):
    ctr = 0
    for word in words:
        if len(words) > 1 and word[0] == word[-1]:
            ctr  += 1

    return ctr
print(match_words(["abc","xyx","pxp","1221"]))
