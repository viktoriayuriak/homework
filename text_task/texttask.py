import os
import urllib
from urllib import request
import requests
import glob
import collections
import re
from collections import Counter

#url = "http://www.gutenberg.org/files/1041/1041.txt"
#r = requests.get(url)
#print(len(r.content))
txt1 = "http://www.gutenberg.org/files/1041/1041.txt"
txt2 = "http://www.gutenberg.org/files/1112/1112.txt"
txt3 = "http://www.gutenberg.org/files/2264/2264.txt"
txt4 = "http://www.gutenberg.org/files/1524/1524.txt"
txt5 = "http://www.gutenberg.org/files/1121/1121.txt"

list_of_urls = [txt1, txt2, txt3, txt4, txt5]
list_of_text = ['text1.txt', 'text2.txt', 'text3.txt','text4.txt','text5.txt']

page1 = urllib.request.urlopen(txt1)
with open('text1.txt', 'wb') as output:
	for x in page1: 
		output.write(page1.read()) 

page2 = urllib.request.urlopen(txt2)
with open('text2.txt', 'wb') as output:
	for x in page2: 
		output.write(page2.read()) 

page3 = urllib.request.urlopen(txt3)
with open('text3.txt', 'wb') as output:
	for x in page3: 
		output.write(page3.read()) 

page4 = urllib.request.urlopen(txt4)
with open('text4.txt', 'wb') as output:
	for x in page4: 
		output.write(page4.read()) 

page5 = urllib.request.urlopen(txt5)
with open('text5.txt', 'wb') as output:
	for x in page5: 
		output.write(page5.read()) 

#concatinate all text files
read_files = glob.glob("*.txt")

with open("result.txt", 'wb') as outfile:
	for f in read_files:
		with open(f, 'rb') as infile:
			outfile.write(infile.read())

def author_name(lines):
    '''Finds the authors name within the docstring'''
    for line in lines:
        name = 'Unknown'
        if line.startswith("Author"):
            line = line.strip('\n')
            line = line.strip('\'')
            author_line = line.split(': ')
            if len(author_line[1]) >=4:   
                name = author_line[1]
            break  # ends the `for` loop, we found an author.

    return "{0:21}{1}".format("Author", name)

words = re.findall(r'\b[a-z]{5,15}\b', open('result.txt').read().lower())
text = Counter(words).most_common(5)

with open('common_words.txt', 'w') as myfile:
	for lines in text:
		myfile.write(' '.join(str(line) for line in lines))
		myfile.write('\n')
#text1 = urllib.request.urlopen("http://www.gutenberg.org/files/1041/1041.txt")
#with open('text1.txt','wb') as output:
# output.write(text1.read())