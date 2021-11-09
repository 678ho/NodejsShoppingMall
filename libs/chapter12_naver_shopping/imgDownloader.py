from urllib.request import urlopen

from bs4 import BeautifulSoup

from libs.chapter12_naver_shopping.naver_shopping_paging import crawl
from libs.chapter12_naver_shopping.parser import parseImg

def imgCrawler():

    n = 1
    imgLink = []

    for i in range(10):
        pageString = crawl(i)
        for j in range(4):
            imgs = parseImg(pageString)[j]
            html = urlopen(imgs).read()
            soup = BeautifulSoup(html,'html.parser')
            img = soup.find_all(class_='_2P2SMyOjl6')


            for i in img:
                imgUrl = i['data-src']
                print(imgUrl)
                with urlopen(imgUrl) as f:
                    with open('react-shop-ko-master/uploads/' + str(n-1) + '.jpg','wb') as h:
                        img = f.read()
                        h.write(img)
                n += 1

imgCrawler()