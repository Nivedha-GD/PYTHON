"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""
import os

def extract_values_and_write():
    directory = '/Users/nanbazhagan/Desktop/practice/2_python_part_2/files'  
    output_file = 'result.txt'  
    values = []

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        if os.path.isfile(file_path):
            with open(file_path, 'r') as f:
                content = f.read().strip()  
                values.append(content)  

    with open(output_file, 'w') as output:
        output.write(', '.join(values))  
    print(f"Values written to {output_file}")

extract_values_and_write()
