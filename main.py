from flask import Flask, jsonify, render_template, request
import requests
import json
import random
import bot



token = "<facebook-token>"

app = Flask(__name__, static_url_path='/static')

@app.route('/response', methods=['GET', 'POST'])
def response():
	answer = "--no response calculated--"
	if request.method == 'POST':
		try:
			data = json.loads(request.data)
			text = data['entry'][0]['messaging'][0]['message']['text'] # Incoming Message Text
			print(text)
			answer = bot.reply(text)
			sender = data['entry'][0]['messaging'][0]['sender']['id'] # Sender ID
			payload = {'recipient': {'id': sender}, 'message': {'text': answer}} # We're going to send this back
			r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload) # Lets send it
		except Exception as e:
			print(e) # something went wrong

	elif request.method == 'GET': # For the initial verification
		if request.args.get('hub.verify_token') == '<facebook-secret-key>':
			return request.args.get('hub.challenge')
		return "Wrong Verify Token"
	
	return answer #Not Really Necessary

@app.route('/dialogflow', methods=['GET', 'POST'])
def dialogflow():
	data = request.get_json(silent=True)
	sentence = data['queryResult']['queryText']
	bot_reply = bot.reply(sentence)

	reply = {
		"fulfillmentText": bot_reply,
	}

	return jsonify(reply)

@app.route("/get")
def get_bot_response():
	userText = request.args.get('msg')
	return str(bot.reply(userText))

@app.route('/')
def home():
	return render_template('index.html')


if __name__ == '__main__':
	app.run()