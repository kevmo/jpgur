import urllib2
import contextlib

from bs4 import BeautifulSoup


def get_images(url):
    with contextlib.closing(urllib2.urlopen(url)) as r:
        html = r.read()
        soup = BeautifulSoup(html)
        og_image = soup.find('meta', attrs={'property': 'og:image'})
        if og_image:
            return og_image.get('content')
        else:
            for img in soup.find_all('img'):
                return img.get('src')