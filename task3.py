### task3 ###

import re
import string
frequency = {}

book_1 = open("book1.txt","r") # read book1
text1 = book_1.read().lower()

book_2 = open("book2.txt","r") # read book2
text2 = book_2.read().lower()

match_pattern1 = re.findall(r'\b[a-z]{0,3}\b', text1)

match_pattern2 = re.findall(r'\b[a-z]{0,3}\b', text2)

for word in match_pattern1:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
 
for words in frequency_list:
    print (words, frequency[words])

fname = raw_input(text2)
try:
    fhand = open(fname)
except:
    print ('text2', fname)
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print ('counts')
