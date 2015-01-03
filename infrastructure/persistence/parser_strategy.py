import logging
import re
import urllib
from bs4 import BeautifulSoup
from dateutil import parser

class CarpeDurham(object):

    url = "http://carpedurham.wordpress.com/page/%d/"
    page = 1
    city = "Durham, NC"

    def first(self):
        self.page = 1
        self.posts = self._posts()
        return self.next()

    def next(self):
        for post in self.posts:
            return post

    def _posts(self):
        page = self._get_page()
        while page is not None:
            soup = BeautifulSoup(page, "html5lib")
            for post in soup.select('.post'):
                title = post.select("h2.storytitle")[0].get_text()
                body = post.select("div.storycontent")[0].get_text()
                date = self._extract_date(post)
                url = post.select("h2.storytitle a[rel=bookmark]")[0].href
                yield {"title": title, "body": body, "date": date, "url": url}
            page = self._get_page()

    def _get_page(self):
        fh = urllib.urlopen(self.url % self.page)
        self.page += 1
        logging.info("Reading: (%(code)d) %(url)s" % \
                {"code": fh.getcode(), "url": fh.geturl()})
        if (fh.getcode() != 200):
            return None
        return fh.read()

    def _extract_date(self, post):
        meta = post.select('div.meta')[0].get_text()
        match = re.search(r"\w+ \d{,2}, \d{4}", meta)
        return parser.parse(match.group(0))
