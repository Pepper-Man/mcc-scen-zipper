import os
import sys
import time
import zipfile
import tkinter as tk
from tkinter import font
from tkinter import filedialog
from tkinter import messagebox

def add_file_to_zip(file_path, zip_file, current_directory):
    zip_file.write(os.path.join(current_directory, 'tags', file_path), arcname=file_path)
    
def tag_grabber(engine, current_directory, scen_name, output_path):
    # Tags that have any of these strings at the start of their filepath will be ignored
    ignore_folders_h2 = {'sound\\', 'sound_remastered\\', 'globals\\', 'shaders\\', 'ai\\', 'cinematics\\', 'rasterizer\\', 'ui\\', 'camera\\', 'effects\\'}
    ignore_folders_h3 = {'sound\\', 'globals\\', 'shaders\\', 'fx\\', 'ai\\', 'cinematics\\', 'rasterizer\\', 'ui\\', 'camera\\', 'effects\\'}
    
    relative_path = 'reports/' + scen_name + '/cache_file_loaded_tags.txt' # Contains all the referenced tag paths
    file_path = os.path.join(current_directory, relative_path)

    try:
        with open(file_path, 'r') as data:
            text = data.readlines()
    except FileNotFoundError:
        print('\nFile not found: ', file_path, '\nDid you build a cache file yet? Please try running the tool again')
        sys.exit()

    tag_paths = []
    tags_missing = 0

    for line in text:
    
        if line.strip('\n') in tag_paths: # Ignore duplicate entries
            continue
        
        if (engine == 'Halo 3'):
            if line[:(line.find('\\') + 1)] in ignore_folders_h3: # Ignore certain folder paths
                continue
        elif (engine == 'Halo 2'):
            test = line[:(line.find('\\') + 1)]
            if test in ignore_folders_h2:
                continue
            
    
        # Grab the year from the last modified date on the file, catch exception if tag doesn't exist
        try:
            modified_timestamp = os.path.getmtime(os.path.join(current_directory, 'tags', line.strip('\n')))
            year = time.gmtime(modified_timestamp).tm_year
        except FileNotFoundError:
            print('\nMissing tag: ' + line.strip('\n'))
            tags_missing += 1
            continue
    
        if (engine == 'Halo 3'):
            if year == 2007: # Tag is from original H3EK, ignore
                continue
        elif (engine == 'Halo 2'):
            if year == 2004: # Tag is from original H2EK, ignore
                continue
    
        tag_paths.append(line.strip('\n'))
    
    zip_file_path = os.path.join(output_path, (scen_name + '.zip'))
    with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
        for tag in tag_paths:
            add_file_to_zip(tag, zip_file, current_directory)
    
    messagebox.showinfo('Success', 'Tags successfully zipped - ' + str(tags_missing) + ' missing tags\n\nZip file written to \"' + output_path + '\"')
    print('\nTags successfully zipped - ' + str(tags_missing) + ' missing tags')

# -------------------- Program enters here -----------------------------

# UI Functions
def browse_folder(folder):
    folder_path = filedialog.askdirectory()
    folder.config(state='normal')
    folder.delete(0, tk.END)
    folder.insert(tk.END, folder_path)
    folder.config(state='readonly')
    
def browse_scenario():
    file_path = filedialog.askopenfilename(filetypes=[('Scenario Tag Files', '*.scenario')])
    scenario_field.config(state='normal')
    scenario_field.delete(0, tk.END)
    scenario_field.insert(tk.END, file_path)
    scenario_field.config(state='readonly')
    
def is_filepath_child(filepath, basepath):
    if os.path.exists(filepath) and os.path.exists(basepath):
        try:
            filepath_drive, filepath_abs = os.path.splitdrive(os.path.abspath(filepath))
            basepath_drive, basepath_abs = os.path.splitdrive(os.path.abspath(basepath))
            
            if filepath_drive.lower() == basepath_drive.lower():
                common_path = os.path.commonpath([filepath_abs, basepath_abs])
                return common_path == basepath_abs
        except OSError:
            pass
    return False
    
def grabber_initialise():
    # Error handling
    if (ek_entry.get() == "") or (scenario_field.get() == "") or (output_entry.get() == ""):
        messagebox.showerror("Error", "Not all paths have been selected.")
    elif not is_filepath_child(scenario_field.get(), ek_entry.get()):
        messagebox.showerror("Error", "Scenario is not in currently selected editing kit.")
        
    # Get values into vars
    root_folder = ek_entry.get()
    scenario_name = scenario_field.get().rsplit('/', 1)[-1].replace('.scenario', '')
    output_path = output_entry.get()
    
    # Run main
    tag_grabber(engine_type, root_folder, scenario_name, output_path)
    

# Window creation
window = tk.Tk()
window.title('MCC Scenario Tags Zipper')
window.geometry('450x400')

# Information header
header_font = font.Font(size=11, weight='bold')
info_label = tk.Label(window, text='Supported: Halo 2, Halo 3, ODST', font=header_font)
info_label.grid(row=0, column=1, padx=5, pady=5)

"""
engine = tk.StringVar(value='Halo 2')
engine_label = tk.Label(window, text="Choose engine type:")
engine_label.grid(row=0, column=1, padx=5, pady=5)
# Engine selection
engine_options = ['Halo 2', 'Halo 3']
engine_dd = tk.OptionMenu(window, engine, *engine_options)
engine_dd.grid(row=1, column=1, padx=5, pady=5)
"""


# Get editing kit location
folder_label = tk.Label(window, text='Select editing kit root folder:')
folder_label.grid(row=2, column=1, padx=5, pady=5)
ek_entry = tk.Entry(window, width=40, state='readonly')
ek_entry.grid(row=3, column=1, padx=20, pady=5)
browse_ek_button = tk.Button(window, text='Browse', command=lambda: browse_folder(ek_entry))
browse_ek_button.grid(row=3, column=2, padx=5, pady=5)

# Get scenario name
scenario_label = tk.Label(window, text='Select your scenario tag:')
scenario_label.grid(row=4, column=1, padx=5, pady=5)
scenario_field = tk.Entry(window, width=40, state='readonly')
scenario_field.grid(row=5, column=1, padx=20, pady=5)
browse_scen_button = tk.Button(window, text='Browse', command=lambda: browse_scenario())
browse_scen_button.grid(row=5, column=2, padx=5, pady=5)

# Get output folder
output_label = tk.Label(window, text='Select an output folder for the zip file:')
output_label.grid(row=6, column=1, padx=5, pady=5)
output_entry = tk.Entry(window, width=40, state='readonly')
output_entry.grid(row=7, column=1, padx=20, pady=5)
browse_out_button = tk.Button(window, text='Browse', command=lambda: browse_folder(output_entry))
browse_out_button.grid(row=7, column=2, padx=5, pady=5)

# Go button
go_label = tk.Button(window, text='Grab all tags!', command=lambda: grabber_initialise())
go_label.grid(row=8, column=1, padx=50, pady=20)

window.mainloop()