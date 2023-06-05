import os
import time
import zipfile

def add_file_to_zip(file_path, zip_file):
    zip_file.write(os.path.join(current_directory, 'tags', file_path), arcname=file_path)

ignore_folders = {'sound\\', 'globals\\', 'shaders\\', 'fx\\', 'ai\\', 'cinematics\\', 'rasterizer\\', 'ui\\', 'camera\\', 'effects\\'}

scen_name = input('Enter your scenario folder name:\n')

current_directory = os.getcwd()
sevzip_path = os.path.join(current_directory, 'bin\\x64\\7zr.exe')
relative_path = 'reports/' + scen_name + '/cache_file_loaded_tags.txt'
file_path = os.path.join(current_directory, relative_path)


with open(file_path, 'r') as data:
    text = data.readlines()

# TODO: Add exception catch ^^

tag_paths = []

for line in text:
    if line[:(line.find('\\') + 1)] in ignore_folders:
        continue
    
    modified_timestamp = os.path.getmtime(os.path.join(current_directory, 'tags', line.strip('\n')))
    year = time.gmtime(modified_timestamp).tm_year
    
    if year == 2007: # Tag is from original EK, ignore
        continue
    
    tag_paths.append(line.strip('\n'))
    
zip_file_path = os.path.join(current_directory, (scen_name + '.zip'))
with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
    for tag in tag_paths:
        add_file_to_zip(tag, zip_file)