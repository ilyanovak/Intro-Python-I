"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

import os

# Attempt 1
# print('os.path.dirname(__file__) = ', os.path.dirname(__file__))
# filename2 = os.path.join(os.path.dirname(__file__), 'foo.txt')
# print('filename2 = ', filename2)

# Attempt 2
# file = open('/src/foo.txt', 'r')
# read_data = file.read()
# print(read_data)
# file.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
