#!/usr/bin/env python2

import re #regular exp package
import requests
from bs4 import BeautifulSoup

def get_url(url):
    #Google user agent for fearfox
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    headers = {'User-Agent': user_agent}
    r = requests.get(url, headers=headers)
    return r.text

def read_page(url):
    soup = BeautifulSoup(get_url(url), 'html.parser') 
    if soup(text=re.compile("Community day", flags=re.I)):
        return True

def get_uris(url):
    soup = BeautifulSoup(get_url(url), 'html.parser') 
    slist = soup.find_all('a',{'class': 'title'})
    #return [x['href'] for x in slist]
    return_value = []
    #list is an array
    for value in slist:
        if value['href'][:3] == '/r/':
             return_value.append(value['href']) #accessing as a dict
    return return_value

def main():
    base_url = "https://old.reddit.com/"
    sub = "TheSilphRoad"
    #print '\n'.join( get_uris(url))
    for uri in get_uris(base_url + "r/" + sub):
        url = base_url + uri
        if read_page(url):
            print url
    
if __name__== '__main__':
    main()
