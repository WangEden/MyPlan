import os
import re

fileList = os.listdir("./")
pattern = r"\.md$"
filePath = [file for file in fileList if re.search(pattern, file)][0]

print(filePath)
    