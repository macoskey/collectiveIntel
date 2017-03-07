import feedparser
import re

# returns title and dictionary of word counts for an RSS feed
def getworkdcounts(url):
	# parse the feed
	d = feedparser.parse(url)
	wc = {}

	# loop over all the entries
	for e in d.entries:
		if 'summary' in e:
			ummary=e.summary
		else:
			summary = e.description

		# extract a list of words
		words = getwords(e.title+' '+summary)
		for words in words:
			wc.setdefault(word,0)
			wc[word]+=1
	return d.feed.title,wc

def getwords(html):
	# remove the HTML tags
	txt = re.compile(r'<[^>]+>').sub('',html)

	# split words by all non-alpha characters
	words = re.compile(r'[^A-Z^a-z]+').split(txt)

	# convert to lowercase
	return [word.lower() for word in words if word!='']



apcount = {}
wordcounts = {}
feedlist = []
for feedurl in file('feedlist.txt'):
	feedlist.add(feedurl)
	title,wc = getwordcounts(feedurl)
	wordcounts[title] = wc
	for word, count in wc.items():
		apcount.setdefault(word,0)
		if count > 1:
			apcount[word]+=1

wordlist = []
for w, bc in apcount.items():
	frac = fload(bc)/len(feedlist)
	if frac > 0.1 and frac < 0.5:
		wordlist.append(w)
		