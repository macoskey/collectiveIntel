import feedparser
import re

# returns title and dictionary of word counts for an RSS feed
def getwordcounts(url):
	# parse the feed
	d = feedparser.parse(url)
	wc = {}

	# loop over all the entries
	for e in d.entries:
		if 'summary' in e:
			summary = e.summary
		else:
			summary = e.description

		# extract a list of words
		words = getwords(e.title+' '+summary)
		for word in words:
	        	wc.setdefault(word,0)
		        wc[word] += 1
	return (d.feed.title,wc)

def getwords(html):
	# remove the HTML tags
	txt = re.compile(r'<[^>]+>').sub('',html)

	# split words by all non-alpha characters
	words = re.compile(r'[^A-Z^a-z]+').split(txt)

	# convert to lowercase
	return [word.lower() for word in words if word != '']



apcount = {}
wordcounts = {}
si = 1
feedlist = [line for line in file('feedlist.txt')]
for feedurl in feedlist:
    try:
        (title,wc) = getwordcounts(feedurl)
        wordcounts[title] = wc
        for word, count in wc.items():
	    apcount.setdefault(word,0)
	    if count > 1:
                apcount[word]+=1
        print '%s successful' % si
        si += 1
    except:
        print 'Failed to parse feed %s' % feedurl

        
wordlist = []
for w, bc in apcount.items():
	frac = float(bc)/len(feedlist)
	if frac > 0.1 and frac < 0.5:
		wordlist.append(w)
	
out = file('blogdata.txt','w')
out.write('Blog')
for word in wordlist: out.write('\t%s' % word)
out.write('\n')
for blog,wc in wordcounts.items():
    # ideal with univode outside the ASCII range
    blog = blog.encode('ascii','ignore')
    out.write(blog)
    for word in wordlist:
        if word in wc: out.write('\t%d' % wc[word])
        else: out.write('\t0')
    out.write('\n')
