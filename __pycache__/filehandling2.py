
"""
'a' => append mode. this would open up the file and append the changes(read, write).
it creates a file if it doesn't exist

'w' => write mode . this allows to write a file. if the file already contains content it will overwrite 
it creates a file if it doesnt exists

'r' => read mode. this is use to read the file. it is the default mode
"""
import imp
import os
import collections
from collections import Counter
from pprint import pprint
fhand= open('file.txt').readlines()
num_lines= 0
frequency ={}
#the setdefault()method returns the value of the item with specified key
#if the key does not exist, insert the key, with the specific value 
for line in fhand:
    for word in line.split():
        frequency.setdefault(word,0)
        frequency[word]+=1
# pprint(frequency)
fhand.close()

# replace a text in the file
with open('file.txt','r+') as file:
    content = file.readlines()
    for line in content:
        if 'TO' in line:
            pos = line.index('TO')
            line =line.replace("TO", 'new text')
    file.seek(0)
    file.writelines(content)
        
