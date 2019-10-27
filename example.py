import nltk
import re
import sys
import json
#to download all nltk.data
#nltk.download('all')

#Note: if this file is run first time, nltk.download('all') line is needed to comment out.

# Usage: python3 example.py "book_title" "book_abstract"

pairs = ""
output = {}

title = sys.argv[1]
abstract = sys.argv[2]
	
book_title = str(title)
book_title = book_title.lower()

book_stract = str(abstract)
book_stract = book_stract.lower()
print(abstract)

input_string = nltk.word_tokenize(book_stract)

tagged = nltk.pos_tag(input_string)
print(tagged)

output["abstract"] = []
for word,tag in enumerate(tagged):
	if tag[1] == "NN" or tag[1] == "NNS" or tag[1] == "NNP" or tag[1] == "NNPS" or tag[1] == "JJ" or tag[1] == "JJR" or tag[1] == "JJS":
		print(tag[0])
		output["title"] = book_title
		output["abstract"].append(tag[0])
print("\n")
print(output)
with open('keyword.json', 'w') as outfile:
    json.dump(output, outfile)

