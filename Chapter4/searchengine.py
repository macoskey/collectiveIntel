# search engine script inspired by Collective Intelligence
# J. Macoskey

class crawler:
     # initialize the crawler with the name of the database
     def __init__(self,dbname): # class initialization
        pass

    def __del__(self): # class deletion parameters
        pass

    def dbcommit(self):
        pass

    # auxilliary function for getting an entry id and adding it if it's not
    # present
    def getentryid(self,table,field,value,createnew=True):
        return None

    # index and individual page
    def addtoindex(self,url,soup):
        print 'Indexing %s' % url

    # extract the text from an HTML page (no tags)
    def gettextonly(self,soup):
        return None

    # separate the words by any non-whitespace character
    def separatewords(self,text):
        return None

    # return true if this url is already indexed
    def isindexed(self,url):
        return False
    
    # add a link between two pages
    def addlinkref(self,urlFrom,urlTo,linkText):
        pass

    # starting with a list of pages, do a breadth first search to the given
    # depth, indexing pages as we go
    def crawl(self,pages,depth = 2):
        pass

    # create the database tables
    def createindextables(self):
        pass


