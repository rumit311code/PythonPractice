"""
File Operations in Python

Options for open() method
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist. Overwrites existing content.
"x" - Create - Creates the specified file, returns an error if the file exists

"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)

file.read() -> all content
file.read(5) -> first 5 characters
file.readLine() -> one line
"""

# 1. Creating and Writing to a File
with open('example.txt', 'w') as file:
    file.write("Hello, this is a sample text.\n")
    file.write("Writing multiple lines.\n")

# 2. Reading from a File
with open('example.txt', 'r') as file:
    content = file.read()
    print("File Content:\n", content)

# 3. Appending to a File
with open('example.txt', 'a') as file:
    file.write("Appending additional line.\n")

# 4. Reading File Line by Line
with open('example.txt', 'r') as file:
    for line in file:
        print("Line:", line.strip())

# 5. Deleting a File
import os
if os.path.exists('example.txt'):
    os.remove('example.txt')
    print("File deleted.")
else:
    print("File does not exist.")

# 6. Checking if a File Exists
if os.path.isfile('example.txt'):
    print("File exists.")
else:
    print("File does not exist.")

# 7. Renaming a File
if os.path.exists('oldname.txt'):
    os.rename('oldname.txt', 'newname.txt')
    print("File renamed.")
else:
    print("File 'oldname.txt' not found.")

# 8. Copying a File
import shutil
shutil.copy('source.txt', 'destination.txt')
print("File copied.")