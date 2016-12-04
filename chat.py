# imports
from chatterbot import ChatBot
from flask import Flask, request, jsonify
app = Flask(__name__)

# starts up a blank chatbot
chatbot = ChatBot(
	'Ron Obvious',
	trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
	silence_performance_warning=True
)

# api request route
@app.route('/', methods=['GET', 'POST'])
def talk(): 
	res = chatbot.get_response(request.get_json()["input"]) # gets a response based on the api post request
	return jsonify(res.serialize()) # sends back response from chatbot

# runs webapp
if __name__ == "__main__":
	app.run(debug=True)
