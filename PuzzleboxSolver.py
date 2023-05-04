import pyperclip
import time

# Get clipboard content
input_string = pyperclip.paste()

# Rest of your code goes here
output_string = ""
for line in input_string.split("\n"):
    # Exclude certain lines
    if line.startswith(('Knot', 'Slide', 'Lockbox', 'Towers', 'Map', 'Click', 'Solved', 'Solving')):
        continue
    directions = []
    i = 0
    while i < len(line):
        if line[i] in ['u', 'd', 'l', 'r']:
            j = i+1
            while j < len(line) and line[j] in ['u', 'd', 'l', 'r']:
                j += 1
            directions.append(line[i:j])
            i = j
        else:
            i += 1
    for direction in directions:
        if direction == "u":
            direction = "{up}"
        elif direction == "d":
            direction = "{down}"
        elif direction == "l":
            direction = "{left}"
        elif direction == "r":
            direction = "{right}"
        output_string += f'Send, {direction}\n'
        output_string += 'Sleep, sleepTime\n'

# Copy output to clipboard
pyperclip.copy("f3:: reload\n"
               "f2:: pause\n"
               "f1:: \n"
               "Random, sleepTime, 110, 135\n"
               + output_string + "Return")

# Print a message to confirm that the output has been copied
print("Output has been copied to clipboard!")
print("Output has been copied to clipboard!")
print("Output has been copied to clipboard!")
