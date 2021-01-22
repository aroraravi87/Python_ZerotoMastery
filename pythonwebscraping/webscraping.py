import requests
import pprint
from bs4  import BeautifulSoup

#refer the BeautifulSoup doc https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#hacker news samle https://news.ycombinator.com/news
# you can use the scrapy framework for messaive data, beautifulsoup is used for small app with limited feature..

def get_scrapping():
    url='https://news.ycombinator.com/news'
    url2='https://news.ycombinator.com/news?p=2'
    res= requests.get(url,verify=False)
    res2= requests.get(url2,verify=False)
    bssoup =BeautifulSoup(res.text,'html.parser')
    bssoup2 =BeautifulSoup(res2.text,'html.parser')
    links=bssoup.select('.storylink')
    subtext=bssoup.select('.subtext')
    links2=bssoup2.select('.storylink')
    subtext2=bssoup2.select('.subtext')
 
    mega_links=links+links2
    mega_subtext=subtext+subtext2
    pprint.pprint(parse_data(mega_links,mega_subtext))
    #print(bssoup.prettify())
    #print(bssoup.body.content)
    #print(bssoup.find_all('div'))
    #print(bssoup.find(id='score_25874526'))
    #print(bssoup.select('.score')) #access throw class
    #print(bssoup.select('#score_25874526')) #access throw class


def parse_data(links,subtext):
    collection=[]
    for idx,item in enumerate(links):
        title=item.getText()
        href=item.get('href',None)
        vote=subtext[idx].select('.score')
        if len(vote):
            points=int(vote[0].getText().replace(' points',''))
        if points>99:
            collection.append({'title':title,'href':href,'votes':points})
    return sort_parse_data_byvote(collection)

def sort_parse_data_byvote(collection):
    return sorted(collection,key=lambda k: k['votes'],reverse=True)


    