
"""
'a' => append mode. this would open up the file and append the changes(read, write).
it creates a file if it doesn't exist

'w' => write mode . this allows to write a file. if the file already contains content it will overwrite 
it creates a file if it doesnt exists

'r' => read mode. this is use to read the file. it is the default mode
"""


fhand=open('file.txt').readlines()#.read()
num_lines=0
for line in fhand:
    # # print(line.strip())                      #for clearing empty spaces in the terminal.
    if not line.isspace():                     #for clearing empty lines when counting 
     num_lines+= 1
print(f'the file contains {num_lines} of text')