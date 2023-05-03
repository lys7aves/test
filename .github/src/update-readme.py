import os
from datetime import datetime

dir_path = "."

def find_target(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        
        if True: # 특정 조건:
            # 수정 날짜 가져오기
            mtime = datetime.fromtimestamp(os.stat(item_path).st_mtime)
            target_list.append([item, item_path, mtime])
            
        if os.path.isdir(item_path):
            find_target(item_path)

target_list = []
find_target(dir_path)

# README.md 파일을 열어 파일 경로를 추가
with open("README.md", "w") as f:
    f.write("# mathematics\n")
    f.write("A collection of notes and solutions on various mathematical topics.\n\n")

    f.write("## List of notes\n")
    for target in target_list:
        f.write("- [{}]({}) - {}\n".format(target))
