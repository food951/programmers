def solution(new_id):
    # 1단계
    new_id = new_id.lower()

    # 2단계
    new_id = ''.join(c for c in new_id if c.islower() or c.isdigit() or c in ['-', '_', '.'])

    # 3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    # 4단계
    if new_id.startswith('.'):
        new_id = new_id[1:]
    if new_id.endswith('.'):
        new_id = new_id[:-1]

    # 5단계
    if not new_id:
        new_id = "a"

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]

    # 마지막에 마침표(.)가 끝에 위치하면 제거
    if new_id.endswith('.'):
        new_id = new_id[:-1]

    # 7단계
    while len(new_id) <= 2:
        new_id += new_id[-1]

    return new_id
