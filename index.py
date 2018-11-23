import requests
from flask import Flask , render_template
app = Flask(__name__)

#hackernews api
r = requests.get('https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty')
data = r.json()
url = []
title = []
for x in range(0,50):
	news = data[x]
	z = f'https://hacker-news.firebaseio.com/v0/item/{news}.json?print=pretty'
	d = requests.get(z)
	v = d.json()
	if v['type'] == 'story':
		try:
			url.append(v['url'])
			title.append(v['title'])
		except KeyError:
			print('went wrong')

json_data = dict(zip(title,url))
# print(json_data)


@app.route("/")
def hello():
	return render_template("index.html",data=json_data.items())
	

