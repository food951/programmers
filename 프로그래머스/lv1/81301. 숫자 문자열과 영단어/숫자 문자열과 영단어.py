def solution(s):
    dic ={"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    result = ""

    i = 0
    while i < len(s):
        for word in dic:
            if s[i:i + len(word)] == word:
                result += str(dic[word])
                i += len(word)
                break
        else:
            result += s[i]
            i += 1

    final_number = int(result)
    return final_number