from chatterbot import ChatBot
from flask import Flask, request, jsonify
app = Flask(__name__)

# import sys

chatbot = ChatBot(
	'Ron Obvious',
	trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
	silence_performance_warning=True
)

@app.route('/', methods=['GET', 'POST'])
def talk(): 
	# print request.get_json(force=True)
	# print request
	# print content
	res = chatbot.get_response(request.get_json()["input"])
	# print res
	# return jsonify("Hi")
	return jsonify(res.serialize())

if __name__ == "__main__":
	app.run(debug=True)