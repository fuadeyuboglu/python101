prompt = "\nTell me something, and I will repeat it back to you: "
prompt +="\nEnter 'quit' to end the program."

message = ""

while message != 'quit':
    message = input(prompt)
    print(message)
    
# Second
prompt = "\nTell me something, and I will repeat it back to you:"
prompt +="\nEnter 'quit' to end the program. "

message = ""

while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':  # does not display the message if it is quit
        print(message)
        
# Flag

prompt = "\nTell me something, and I will repeat it back to you:"
prompt +="\nEnter 'quit' to end the program. "

active = True

while active:
    message = input(prompt)
    
    if message == 'quit':  
        active = False
    else:
        print(message)
