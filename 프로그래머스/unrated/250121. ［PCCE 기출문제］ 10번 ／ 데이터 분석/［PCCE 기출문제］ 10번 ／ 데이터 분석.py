def solution(data, ext, val_ext, sort_by):
    header = ["code", "date", "maximum", "remain"]
    
    # ext에 해당하는 열의 인덱스 찾기
    ext_index = header.index(ext)
    
    # 조건에 맞는 데이터 필터링
    filtered_data = [item for item in data if item[ext_index] < val_ext]
    
    # sort_by에 해당하는 열의 인덱스 찾기
    sort_by_index = header.index(sort_by)
    
    # 정렬하여 결과 반환
    sorted_data = sorted(filtered_data, key=lambda x: x[sort_by_index])
    
    return  sorted_data