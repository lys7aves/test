import os

dir_path = "."
file_paths = []

# 디렉토리와 그 하위 디렉토리에서 파일 경로를 추출하여 file_paths 리스트에 추가
for root, directories, files in os.walk(dir_path):
    for filename in files:
        file_path = os.path.join(root, filename)
        file_paths.append(file_path)

# README.md 파일을 열어 파일 경로를 추가
with open("README.md", "w") as f:
    f.write("## 파일 목록\n\n")
    for file_path in file_paths:
        f.write("- {}\n".format(file_path))
