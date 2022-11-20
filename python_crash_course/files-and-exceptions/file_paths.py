# Relative file path

""" A relative file path tells Python to look for a given
    location relative to the directory where the currently
    running program file is stored. """

with open('text_files/filename.txt') as file_object: 
    
""" Windows systems use a backslash (\) instead of a forward slash (/)
    when displaying file paths, but you can still use forward slashes 
    in you code. """

# Absolute file paths

""" Absolute paths are usually longer than relative paths,
    so it's helpful to assign them to a variable and then
    pass that variable to open(): """

file_path = '/home/etmatthes/other_files/text_files/filename.txt'
with open(file_path) as file_object:
