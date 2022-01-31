# Program to read a text file line by line and display each word separated by a '#'

with open('Files/text.txt', 'r') as f:
    for line in f:
        print(line.replace(' ','#'))