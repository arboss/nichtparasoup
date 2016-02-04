
import re

try:
    from urllib.parse import urljoin    # py3
except ImportError:
    from urlparse import urljoin        # py2

from . import Crawler, CrawlerError


class Pr0gramm(Crawler):
    """ pr0gramm.com image provider"""

    ## class constants

    ## properties

    __uri = ""
    __next = ""
    __site = ""

    __filter = re.compile('^/static/[\d]+')
    __filterNextPage = ""

    ## functions

    @staticmethod
    def __build_uri(uri):
        return uri

    def _restart_at_front(self):
        self.__next = self.__uri

    def __init__(self, uri, site):
        self.__site = site
        self.__uri = self.__class__.__build_uri(uri)
        self.__filterNextPage = re.compile('^/static/' + self.__site + '/[\d]+')
        self._restart_at_front()

    def _crawl(self):
        uri = self.__next
        self.__class__._log("debug", "%s crawls url: %s" % (self.__class__.__name__, uri))

        (page_container, base, _) = self.__class__._fetch_remote_html(uri)
        if not page_container:
            self.__class__._log("debug", "%s crawled EMPTY url: %s" % (self.__class__.__name__, uri))
            return

        pages = page_container.findAll("a", href=self.__filter)
        images_added = 0
        for page in pages:
            if self.__crawl_page(urljoin(base, page["href"])):
                images_added += 1

        # Paging
        nextPageLink = page_container.find("a", href=self.__filterNextPage)
        self.__next = urljoin(base, nextPageLink["href"])

        self.__class__._log("debug", "%s set next Page: %s" % (self.__class__.__name__, self.__next))

        if not images_added:
            self.__class__._log("debug", "%s found no images on url: %s" % (self.__class__.__name__, uri))

    def __crawl_page(self, uri):
        (page, base, _) = self.__class__._fetch_remote_html(uri)
        if not page:
            self.__class__._log("debug", "%s sub-crawled EMPTY url: %s" % (self.__class__.__name__, uri))
            return False

        image = page.find("img", {"src": True})
        if not image:
            return False

        return self._add_image(urljoin(base, image["src"]), self.__site)
