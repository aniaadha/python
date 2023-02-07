import os

#split name of path
split_path = os.path.splitext("project/file_name.py")

#print head of path
print(split_path[0])

#print extension
print(split_path[1])