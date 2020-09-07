"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

import os

print('absolute path', os.path.dirname(os.path.abspath(__file__)))
filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'foo.txt')
print('filename = ', filename)

with open(filename, 'r') as f:
    read_data = f.read()
    print(read_data)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

print('absolute path', os.path.dirname(os.path.abspath(__file__)))
filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bar.txt')
print('filename = ', filename)

with open(filename, 'w') as f:
    write_data = "An ocean voyage.\nAs waves break over the bow,\nthe sea welcomes me."
    read_data = f.write(write_data)

with open(filename, 'r') as f:
    read_data = f.read()
    print(read_data)
