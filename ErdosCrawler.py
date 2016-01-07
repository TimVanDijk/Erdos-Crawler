import urllib.request
import re

class ErdosCrawler:
    start_url = 'http://dblp.uni-trier.de/pers/hd/e/Erd=ouml=s:Paul'
    target_url = None
    queue = []
    closed = []

    def __init__(self, target_url):
        self.target_url = target_url

    def _extract_urls(self, page):
            #The list of coauthors is always on the same line, namely 23
            line = page.readlines()[22]
            urls = re.findall('http://dblp.uni-trier.de/pers/hd/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(line))
            return urls

    def crawl(self):
        self.queue.append((self.start_url, 0, []))
        while len(self.queue) > 0:
            el = self.queue.pop(0)
            cur_url = el[0]
            number = el[1]
            path = el[2]
            self.closed.append(el[0])
            print(str(number) + ' - ' + str(cur_url))
            with urllib.request.urlopen(cur_url) as page:
                urls = self._extract_urls(page)
                for url in urls:
                    if url == self.target_url:
                        return number + 1, el[2].append(url)
                    elif url not in self.closed:
                        self.queue.append((url, number + 1, [url].append(path)))