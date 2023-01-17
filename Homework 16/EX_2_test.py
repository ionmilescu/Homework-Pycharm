
from File_functions import create_file, print_out_contents
import os

file_name = create_file()
show_content = file_name.readlines()
print(show_content)