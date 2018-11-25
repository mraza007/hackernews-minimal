import requests
from flask import Flask , render_template
from flask_mail import Mail, Message
app = Flask(__name__)

app.config.update(mail_settings)
mail = Mail(app)
@app.route("/")
def home():
	# hackernews api
	r = requests.get('https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty')
	data = r.json()
	url = []
	title = []
	for x in range(0,100):
		news = data[x]
		z = f'https://hacker-news.firebaseio.com/v0/item/{news}.json?print=pretty'
		d = requests.get(z)
		v = d.json()
		if v['type'] == 'story':
			try:
				url.append(v['url'])
				title.append(v['title'])
			except KeyError:
				pass
	json_data = dict(zip(title,url))
	# print(json_data)
	return render_template('index.html',data=json_data.items())

if __name__ == '__main__':
	app.run()