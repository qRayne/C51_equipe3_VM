from distutils import dir_util
import os


dirs_paths = []
files_paths = []
for root, dirs, files in os.walk("./Structure", topdown=False):
    for name in files:
        full_name = os.path.join(root, name)
        files_paths.append(full_name)
    for name in dirs:
        full_name = os.path.join(root, name)
        dirs_paths.append(full_name)
        
    
print(f'{dirs_paths=}')
print(f'{files_paths=}')

for path in files_paths:
    with open(path, 'r') as f:
        for line in f:
            print(line)