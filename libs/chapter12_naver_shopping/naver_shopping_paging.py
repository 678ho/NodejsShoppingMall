import requests


from libs.chapter12_naver_shopping.parser import parse, parseL
from pymongo import MongoClient

from libs.chapter12_naver_shopping.sdf import count

cluster = MongoClient("mongodb+srv://678ho:rhkdgh14@cluster0.pfo6l.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = cluster["<dbname>"]
collection = db["products"]
posts = db.posts

def crawl(pageNo):
    url = "https://search.shopping.naver.com/search/all?frm=NVSCTAB&pagingIndex={}&pagingSize=20&productSet=total&query=%EA%B3%B5%EC%9C%A0%EA%B8%B0&sort=rel&timestamp=&viewType=list".format(
        pageNo)
    data = requests.get(url)
    return data.content

def update(i):
        collection.find_one_and_update({"images":" "}, {"$set": {"images": "uploads\\{}.jpg".format(i)}})

def dbCount():
    print(posts.count())

def insert(num):
    x = collection.insert_many(totalProducts[num])


totalProducts = []
totalLinks = []
for pageNo in range(1, 10 + 1):
    pageString = crawl(pageNo)
    products = parse(pageString)
    links = parseL(pageString)
    totalProducts.append(products)
    totalLinks.append(links)

    #print(totalLinks)
    #print(totalProducts)
    #insert(pageNo-1)

#for i in range(count()):
    #update(i)



