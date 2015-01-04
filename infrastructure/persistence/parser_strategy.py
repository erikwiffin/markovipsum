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
    meta = post.select(selector)[0].get_text()
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


class TriangleExplorer(ParserStrategy):

    url = "http://triangleexplorer.com/page/%d/"
    city = "Durham, NC"

    selectors = {
            "title": "h2.entry-title",
            "body": "div.entry-content",
            "url": "h2.entry-title a[rel=bookmark]",
            "date": "div.entry-meta"}


class CarpeDurham(ParserStrategy):

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
