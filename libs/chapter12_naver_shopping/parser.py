from bs4 import BeautifulSoup
import datetime

def getProductLink(li):
    aTit = li.find("a", {"class": "basicList_link__1MaTN"})
    return aTit['href']
def parseL(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find("ul", {"class" : "list_basis"})
    lis = ul.findAll("li",{"class":"basicList_item__2XT81"})

    links = []
    for li in lis:
        try:
            link = getProductLink(li)
            links.append(link)
        except:
            print("--error--")
    return links

def getProductInfo(li):
    priceReload = li.find("span", {"class":"price_num__2WUXn"})
    aTit = li.find("a",{"class":"basicList_link__1MaTN"})
    aDes = li.find("div",{"class":"basicList_detail_box__3ta3h"})
    title = str(aTit.get_text())
    description = str(aDes.get_text())

    return {"title":title,
            "price":priceReload.text.replace("원","").replace(",",""),
            "description":description,
            "images":" ",
            "continents":1,
            "views":0,
            "sold":0,
            "createdAt":datetime.datetime.utcnow(),
            "updatedAt":datetime.datetime.utcnow(),
            "__v":"0",
            "Link": aTit['href']
            }
def getProductImg(li):
    aTit = li.find("a",{"class":"basicList_link__1MaTN"})
    img = aTit['href']
    #print(img)
    return img

def parseImg(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find("ul", {"class": "list_basis"})
    lis = ul.findAll("li", {"class": "basicList_item__2XT81"})

    imgs = []
    for li in lis:
        try:
            #print(imgs)
            img = getProductImg(li)
            imgs.append(img)
        except:
            print("--error--")
    return imgs

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find("ul", {"class" : "list_basis"})
    lis = ul.findAll("li",{"class":"basicList_item__2XT81"})

    products = []
    links = []
    for li in lis:
        try:
            product = getProductInfo(li)
            products.append(product)
        except:
            print("--error--")
    return products



