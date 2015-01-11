import logging, re, urllib
from bs4 import BeautifulSoup
from dateutil import parser

def text(post, selector):
    try:
        return post.select(selector)[0].get_text()
    except AttributeError:
        print post, selector
        raise

def href(post, selector):
    return post.select(selector)[0]['href']

def extract_date(post, selector):
    meta = text(post, selector)
    match = re.search(r"\w+ \d{,2}, \d{4}", meta)
    return parser.parse(match.group(0))


class ParserStrategy(object):

    url = ""
    city = ""

    selectors = {}

    def first(self):
        self.page = 1
        self.posts = self._posts()
        return self.next()

    def next(self):
        for post in self.posts:
            return post

    def _get_page(self):
        fh = urllib.urlopen(self.url % self.page)
        self.page += 1
        logging.info("Reading: (%(code)d) %(url)s" % \
                {"code": fh.getcode(), "url": fh.geturl()})
        if (fh.getcode() != 200):
            return None
        return fh.read()

    def _posts(self):
        page = self._get_page()
        while page is not None:
            soup = BeautifulSoup(page, "html.parser")
            for post in soup.select(".post"):
                title = text(post, self.selectors["title"])
                body = text(post, self.selectors["body"])
                date = extract_date(post, self.selectors["date"])
                url = href(post, self.selectors["url"])
                yield {"title": title, "body": body, "date": date, "url": url}
            page = self._get_page()


class CarpeDurham(ParserStrategy):

    url = "http://carpedurham.com/page/%d/"
    city = "Durham, NC"

    selectors = {
            "title": "#content .title",
            "body": "#content .entry",
            "url": ".title a[rel=bookmark]",
            "date": "#stats span:nth-of-type(2)"}

    def _posts(self):
        page = self._get_page()
        while page is not None:
            soup = BeautifulSoup(page, "html.parser")
            for post in soup.select("#front-list .clearfloat"):
                url = href(post, self.selectors["url"])
                full_post = self._full_post(url)
                title = text(full_post, self.selectors["title"])
                body = self.extract_body(full_post, self.selectors["body"])
                date = self.extract_date(full_post, self.selectors["date"])
                yield {"title": title, "body": body, "date": date, "url": url}
            page = self._get_page()

    def _full_post(self, url):
        fh = urllib.urlopen(url)
        logging.info("Reading: (%(code)d) %(url)s" % \
                {"code": fh.getcode(), "url": fh.geturl()})
        return BeautifulSoup(fh.read(), "html.parser")

    def extract_body(self, post, selector):
        body = text(post, selector)
        body = re.sub(r'Carpe Durham does not issue ratings.*', '', body)
        body = re.sub(r'No members have expressed a view.*', '', body)
        body = re.sub(r'I generally agree.I generally disagree.', '', body)
        return body

    def extract_date(self, post, selector):
        meta = text(post, selector)
        match = re.search(r"\d{,2} \w+ \d{4}", meta)
        return parser.parse(match.group(0))


class TriangleExplorer(ParserStrategy):

    url = "http://triangleexplorer.com/page/%d/"
    city = "Durham, NC"

    selectors = {
            "title": "h2.entry-title",
            "body": "div.entry-content",
            "url": "h2.entry-title a[rel=bookmark]",
            "date": "div.entry-meta"}


class CarpeDurhamWordpress(ParserStrategy):

    url = "http://carpedurham.wordpress.com/page/%d/"
    city = "Durham, NC"

    selectors = {
            "title": "h2.storytitle",
            "body": "div.storycontent",
            "url": "h2.storytitle a[rel=bookmark]",
            "date": "div.meta"}

class TriangleFoodBlog(ParserStrategy):

    url = "http://trianglefoodblog.com/?paged=%d"
    city = "Durham, NC"

    selectors = {
            "title": "h2.entry-title",
            "body": "div.entry-content",
            "url": "h2.entry-title a[rel=bookmark]",
            "date": "div.entry-meta"}
