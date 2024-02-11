import os

# get current path
path = os.getcwd()

# getting list of all files in a path
files = os.listdir(path)

# getting list of files with specific extenzion in path
text_files = [f for f in os.listdir(path) if f.endswith('.txt')]

# split file name from extension
# -> ['file','.txt']
os.path.splittext('file.txt') 

# copy file
os.system('cp source.txt destination.txt')  

# saving output os a command in a variable
data = os.popen('cat /etc/services').read()

