import requests
# hackernews api
r = requests.get('https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty')
data = r.json()

def hacker_news():
	for x in range(0,30):
		news = data[x]
		z = f'https://hacker-news.firebaseio.com/v0/item/{news}.json?print=pretty'
		d = requests.get(z)
		v = d.json()
		if v['type'] == 'story':
			print(f'{x} ' + "Title: "+ v['title'] + '-' +"\n" + "url: "+v['url'])


