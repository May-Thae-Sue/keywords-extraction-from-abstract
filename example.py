import nltk
import re
import json
#to download all nltk.data
nltk.download('all')

pairs = ""
filtered_output = []
output = {}
with open('book.json', 'r') as input_file:
	data = json.load(input_file)
	
	title = [x for x in data]
	book_title = str(title)
	book_title = book_title.lower()
	book_title = book_title.replace("['","")
	book_title = book_title.replace("']","")
	#print(book_title)

	abstract = [data[x] for x in data]
	book_stract = str(abstract)
	book_stract = book_stract.lower()
	book_stract = book_stract.replace("['","")
	book_stract = book_stract.replace("']","")
#	print("THIS IS ABSTRACT")
	print(abstract)

	input_string = nltk.word_tokenize(book_stract)
	#print(input_string)

	tagged = nltk.pos_tag(input_string)
#	print("THIS IS TAG")
	print(tagged)

	output[book_title] = []
	for tagged_pairs in tagged:
		pairs= pairs.join(tagged_pairs)
		pattern = r'(^.*NN$)|(^.*NNS$)|(^.*NNP$)|(^.*NNPS$)|(^.*JJ$)|(^.*JJR$)|(^.*JJS$)'
		match =  re.match(pattern,pairs, re.I)
		if match:
			output[book_title].append(tagged_pairs[0])
		pairs = ""

with open('keyword.json', 'w') as outfile:
    json.dump(output, outfile)


