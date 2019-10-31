from flask import Flask, jsonify, make_response, request
import nltk
app = Flask(__name__)

output = []

@app.route('/',methods=['POST'])
def extract():
	data = request.get_json()
	nltk.data.path.append('./nltk_data/')
	title = data['title']
	abstract = data['abstract']

	book_title = title.lower()

	book_stract = abstract.lower()

	input_string = nltk.word_tokenize(book_stract)

	tagged = nltk.pos_tag(input_string)

	for word,tag in enumerate(tagged):
		if tag[1] == "NN" or tag[1] == "NNS" or tag[1] == "NNP" or tag[1] == "NNPS" or tag[1] == "JJ" or tag[1] == "JJR" or tag[1] == "JJS":
			output.append(tag[0])

	return make_response(jsonify({
	"title" : book_title,
	"abstract" : output
	}),200)

if __name__ == '__main__':
   app.run(host = "127.0.0.1",port = "5000",debug=True)
