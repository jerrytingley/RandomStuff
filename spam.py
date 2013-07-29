from urlparse import urljoin as join
from urllib2 import urlopen as get
from BeautifulSoup import BeautifulSoup

def build_database(start_url, debug=False):
    urls = [start_url]
    emails = []
    for url in urls:
        try:
            if debug: print url
            soup = BeautifulSoup(get(url).read())
            for link in soup.findAll('a', href=True):
                if link['href'].startswith('mailto:'):
                    emails.append(link['href'].replace('mailto:', ''))
                    if debug: print "[!!] Email: "+link['href']
                else:
                    u = join(url, link['href'])
                    urls.append(u)
                    if debug: print u
            urls = list(set(urls))
            emails = list(set(emails))
        except Exception as e:
            #print "[!!!!!] EXCEPTION: "+str(e)
            #return list(emails)
            pass
    return list(emails)

print build_database(some_url, debug=True)
