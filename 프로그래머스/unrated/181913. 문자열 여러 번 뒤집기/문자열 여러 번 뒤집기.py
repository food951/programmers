def solution(my_string, queries):
    answer = ''
    list_str=list(my_string) # 문자열을 list 형태로 변환
    query= []               # 
    for i in range(len(queries)): 
        query = list_str[queries[i][0]:queries[i][1]+1] # queries의 배열로 슬라이싱
        query.reverse()  # 그걸 뒤집음
        list_str[queries[i][0]:queries[i][1]+1] = query # 뒤집은 query값을 다시 원래 위치에 대체
    
    answer = "".join(list_str) # 리스트를 문자열로 변환
    return answer