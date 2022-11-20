with open('pi_digits.txt') as file_object:
    contents = file_object.read()

print(contents)

""" You could open and close the file by calling open() and close(),
    but if a bug in you program prevents the close() method from
    being executed, the file may never close. Improperly closed files
    can cause data to be lost or corrupted. """
