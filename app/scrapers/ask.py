from __future__ import print_function
from generalized import Scraper


class Ask(Scraper):
    """Scrapper class for Ask"""

    def __init__(self):
        self.url = 'http://ask.com/web'
        self.defaultStart = 1
        self.startKey = 'page'

    def nextStart(self, currentStart, prevResults):
        return currentStart + 1

    def parseResponse(self, soup):
        """ Parse the response and return set of urls
        Returns: urls (list)
                [[Tile1,url1], [Title2, url2],..]
        """
        urls = []
        for div in soup.findAll('div', {'class': 'PartialSearchResults-item'}):
            title = div.div.a.text
            url = div.div.a['href']
            urls.append({'title': title, 'link': url})
        return urls
