import os
import os.path
import shutil

# create a folder parents
# os.mkdir('folder1')

# a = os.listdir('.')
# print(a)

# x = os.path.exists('fernando.txt')
# print(x)

# y = os.path.exists('folder1')
# print(f" The existance of the folder is: {y}")

# remove folder1
# os.rmdir('folder1')
# a = os.listdir('.')
# print(a)

shutil.rmtree('parents')
a = os.listdir('.')
print(a)
