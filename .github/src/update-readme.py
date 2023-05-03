import os
from datetime import datetime
import re

# 탐색할 root 경로
dir_path = "."

# ignore 파일을 읽어서 패턴 목록을 리스트로 저장
with open('./.github/config/.ignore', 'r') as f:
    ignore = f.readlines()
patterns = []
for p in ignore:
    pattern = r""
    for c in p:
        if c == '*':
            pattern = pattern + r".*"
        elif c in ".^$*+?{}[]|()":  # 메타 문자
            pattern = pattern + r"[{}]".format(c)
        else:
            pattern = pattern + r'{}'.format(c)
    patterns.append(pattern)

print(patterns)
    
# ignore 패턴과 일치하는지 확인하는 함수
def check_ignore_pattern(item_path):
    for pattern in patterns:
        if re.fullmatch(pattern, item_path[2:]):  # 항상 붙는 "./" 제거
            return True
    return False


def find_target(path, level):
    cnt = 0
    
    # 하위 디렉토리 순환
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        
        if check_ignore_pattern(item_path): # ignore 조건을 만족하면 무시
            continue
            
        # 파일(혹은 디렉토리) 리스트에 추가하기
        mtime = datetime.fromtimestamp(os.stat(item_path).st_mtime)  # 수정 날짜 가져오기
        target_list.append([level, item, item_path, mtime])
        cnt += 1
        
        # 디렉토리면 하위 디렉토리 탐색
        if os.path.isdir(item_path):
            res = find_target(item_path, level+1)
            if res == 0:  # 만약 하위 디렉토리에 아무것도 없으면 현재 디렉토리도 삭제
                target_list.pop()
                cnt -= 1
                

target_list = []
find_target(dir_path, 0)

# README.md 파일을 열어 파일 경로를 추가
with open("README.md", "w") as f:
    f.write("# mathematics\n")
    f.write("A collection of notes and solutions on various mathematical topics.\n\n")

    f.write("## List of notes\n")
    for target in target_list:
        for level in range(target[0]):
            f.write("  ")
        f.write("- [{}]({}) - {}\n".format(target[1], target[2], target[3]))
