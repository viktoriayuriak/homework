import collections
import re
from collections import Counter

words = re.findall(r'\b[a-z]{5,15}\b', open('result.txt').read().lower())
text = Counter(words).most_common(5)

with open('common_words.txt', 'w') as myfile:
	for lines in text:
		myfile.write(' '.join(str(line) for line in lines))
		myfile.write('\n')