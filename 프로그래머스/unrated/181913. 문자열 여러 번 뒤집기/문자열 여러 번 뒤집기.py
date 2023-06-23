def solution(my_string, queries):
    answer = ''
    b = []
    list_str=list(my_string)
    for i in range(len(queries)):
        b = list_str[queries[i][0]:queries[i][1]+1]
        b.reverse()
        list_str[queries[i][0]:queries[i][1]+1] = b
    
    answer = "".join(list_str)
    return answer