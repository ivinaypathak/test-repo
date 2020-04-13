import os
from datetime import datetime

# Getting the current working directory
print(os.getcwd())

# Changing the current working directory
# os.chdir('/Users/Vinay Pathak/Desktop/')

# print(os.getcwd())

#-------------------------------------------------------------------------------------------------------#

# Listing all the files and folders of the current working directory
# print(os.listdir())

# Creating new folder in current working directory
# os.mkdir('OS_Module_Dir1/Sub-Dir-1')   # This will throw an error because the parent diretory OS_Module_Dir1 does not exists
# os.rmdir('OS_Module_Dir1') # To remove the directory

# os.makedirs('OS_Module_Dir2/Sub-Dir-2')# This will create the sub-level directory if the parent directory does not exists even
# os.removedirs('OS_Module_Dir2/Sub-Dir-1')  # To remove the subb level directory

#-------------------------------------------------------------------------------------------------------#

# ROUGH WORK
path = '/Users/Vinay Pathak/Desktop/python' + r'\class.mkv'
print(path.replace('\\', '/'))
a, b = os.path.split(path.replace('\\', '/'))
print(a)
print(b)
# os.makedirs('VLC File')
# os.chdir(a[1:] + '/' + 'Text File')
# file_path = os.path.join('Text File', b)
# open(os.path.join('VLC File', b), 'wb').close()
if(not os.path.exists(a + '/VLC File')):
    os.makedirs('VLC File')
os.rename('/Users/Vinay Pathak/Desktop/python/class.mkv', a + '/VLC File/' + b)  # Moving The File From python to VLC File

#-------------------------------------------------------------------------------------------------------#

# Renaming the file name
# os.rename('log.txt', 'log_file.txt')

#-------------------------------------------------------------------------------------------------------#

# Getting the status of the file or directory

# print(os.stat('test.py'))
# mod_time = os.stat('log_file.txt').st_mtime
# print(datetime.fromtimestamp(mod_time))

#-------------------------------------------------------------------------------------------------------#
# TRAVERSING THE DIRECTORY TREE
# for dirpath, dirnames, filenames in os.walk('/Users/Vinay Pathak/Desktop/'):
#     print('Current Path:', dirpath)
#     print('Directories:', dirnames)
#     print('Files:', filenames)
#     print()

#-------------------------------------------------------------------------------------------------------#

# print(os.environ.get('HOME'))

# file_path = os.path.join(os.environ.get('HOME'),'test.txt')

# print(file_path)

#-------------------------------------------------------------------------------------------------------#

# basename is the file name at the end of the path
# print(os.path.basename('/Users/Vinay Pathak/Desktop/log_file.txt'))


# If we want to get the directory name at the end of the path
# print(os.path.dirname('/Users/Vinay Pathak/Desktop/log_file.txt'))

# If to get both the file name and the directory name
# print(os.path.split('/Users/Vinay Pathak/Desktop/log_file.txt'))
# a, b = os.path.split('/Users/Vinay Pathak/Desktop/log_file.txt')
# print(a[1:])
# print(b)

#-------------------------------------------------------------------------------------------------------#

# SOME OTHER USEFUL METHODS
# print(os.path.exists('/Users/Vinay Pathak/Desktop/log_file.txt'))  # Likewise we can check for directory also

# print(os.path.isdir('/Users/Vinay Pathak/Desktop/'))

# print(os.path.isfile('/Users/Vinay Pathak/Desktop/log_file.txt'))

# Parsing out the extension and the file name
# print(os.path.splitext('/Users/Vinay Pathak/Desktop/log_file.txt'))
# directory, file_ext = os.path.splitext('/Users/Vinay Pathak/Desktop/log_file.txt')
# print(directory)
# print(file_ext)
#-------------------------------------------------------------------------------------------------------#

# TO CHECK THE METHOD AND ATTRIBUTES PRESENT IN OS MODULE
# print(dir(os.path))
