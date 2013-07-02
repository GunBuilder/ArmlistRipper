from pyquery import *
from time import sleep
 
class Firearm:
        def __init__(self, title, href, price, location):
                self.title = self.clean(title)
                self.href = self.clean(href)
                self.price = self.clean(price)
                self.location = location
        def clean(self, instr):
                return str(instr).strip()
        def __str__(self):
                return "Title: {0} - ${1}".format(self.title, self.price)
 
def scrapeListing(list_url):
        print(list_url['href'])
        full_url="http://www.armslist.com"+str(list_url['href'])
        print(full_url)
        html = PyQuery(url=full_url)
        title = html("article.post-details h1.title").text()
        href = list_url
        price = html("article.post-details dd.price").text()
        location = html("article.post-details dd.location").text()
        print(title, price)
 
def scrapePage(myurl):
        list_urls = []
        html = PyQuery(url=myurl)
        listings = html('div.listings-area article.post')
        fireobjs = []
        for post in listings:
                href = post[2][0][0].attrib
                print(href)
                list_urls.append(href)
        return list_urls
 
def scrape(pagelimit = 1):
        myurl = "http://www.armslist.com/classifieds/search?location=usa&category=guns&page={0}&posttype=1&tag=pistol"
        fireobjs = []
        for i in range(pagelimit):
                print("Page " + str(i) + "...")
                fireobjs.extend( scrapePage(myurl.format(str(i))) )
                print(len(fireobjs))
                print(fireobjs)
                sleep(1)
        return fireobjs
 
if __name__ == '__main__':
        fire_obs = []
        list_urls = scrape(1)
        for item in list_urls:
                print(item)
                scrapeListing(item)