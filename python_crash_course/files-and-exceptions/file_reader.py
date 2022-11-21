with open('pi_digits.txt') as file_object:
    contents = file_object.read()

print(contents)

""" You could open and close the file by calling open() and close(),
    but if a bug in you program prevents the close() method from
    being executed, the file may never close. Improperly closed files
    can cause data to be lost or corrupted. """

# Reading line by line
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
        
""" .rstrip(): blank lines appear because an invisible
    newline character is at the end of each
    line in the text file. so rstrip is used. """

# Making a list of lines from a file
""" To retain access to a file's contents outside
    the with block and then work with that list. """

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.rstrip())
