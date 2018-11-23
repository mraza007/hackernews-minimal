import requests
from flask import Flask , render_template
from flask_mail import Mail, Message
app = Flask(__name__)

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
			

json_data = dict(zip(title,url))
# print(json_data)

mail_settings = {
    "MAIL_SERVER": 'YOUR STMP SERVER',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": '',
    "MAIL_PASSWORD": ''
}
app.config.update(mail_settings)
mail = Mail(app)
@app.route("/")
def email():
	msg = Message(subject="Hacker News",
	              sender=app.config.get("MAIL_USERNAME"),
	              recipients=[""], # replace with your email for testing
	              html=render_template('index.html',data=json_data.items()))
	mail.send(msg)
	return "sent"

	



