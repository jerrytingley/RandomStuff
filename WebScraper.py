import os
import mechanize
from random import choice
from urllib import urlretrieve as get

class WebScraper:
    def __init__(self, urls, rand_ua = True, robots = True):
        self.urls = urls
        self.__br = mechanize.Browser()
        if not robots: self.__br.set_handle_robots(False)
        if rand_ua:
            self.__user_agent = self.__random_user_agent()
            self.__br.addheaders = [('User-agent', self.__user_agent)]

    __random_user_agent = lambda self: choice(['Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)'])
    __file_encode       = lambda self, x: x.replace("'",'').replace('/','').replace('?','').replace('<','').replace('>','').replace('\\','').replace(':','').replace('*','').replace('|','').replace('"','').replace('%20', ' ')
    __folder_encode     = lambda self, x: '_'.join(x.split('/')[2:-1])+'/'
    __is_dir            = lambda self, x: True if x.endswith('/') else False

    def download(self, follow_par_dir = False, verbose = True, ext = ''):
        if verbose: print "[*] Starting WebScraper"
        for url in self.urls:
            self.__br.open(url)
            fol = self.__folder_encode(url)
            if not os.path.exists(self.__folder_encode(url)):
                os.mkdir(self.__folder_encode(url))
            if verbose: print "[*] Scraping: ", self.__br.title()
            
            for link in self.__br.links():
                url_ = link.absolute_url
                try:
                    if not self.__is_dir(url_) and link.url[0:3] != '?C=' and url_.split('.')[-1] in ext:
                        if verbose: print "[!] Downloading: ", self.__file_encode(url_.split('/')[-1])
                        get(url_, fol+self.__file_encode(url_.split('/')[-1]))
                    else:
                        if url_ not in self.urls and follow_par_dir and link.url[0:3] != '?C=' and self.__is_dir(url_):
                            if verbose: print "[*] Adding parent directory ",url_," to the URL Queue"
                            self.urls.append(url_)
                        elif url_ not in self.urls and not follow_par_dir and url_ == '/'.join(link.base_url.split('/')[0:-2])+'/':
                            continue
                except Exception, err:
                    print "[!!] ", err
                    pass

robot = WebScraper(['http://boards.4chan.org/tv/res/28390386'], robots = False)
robot.download('png', 'jpg')
