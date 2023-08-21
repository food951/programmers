def solution(s):
    words = s.split(" ")  # 단어로 분할
    answord = ""

    for i, word in enumerate(words):
        for j in range(len(word)):
            if j % 2 == 0:
                answord += word[j].upper()
            else:
                answord += word[j].lower()
        
        if i < len(words) - 1:
            answord += ' '

    return answord