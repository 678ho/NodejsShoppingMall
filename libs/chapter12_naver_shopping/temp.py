import requests
from bs4 import BeautifulSoup

# from libs.chapter12_naver_shopping.naver_shopping_paging import crawl
# from libs.chapter12_naver_shopping.parser import parse, parseL
#
# totalLinks = []
# for pageNo in range(1, 10 + 1):
#     pageString = crawl(pageNo)
#     links = parseL(pageString)
#     totalLinks.append(links)
#     #base_url = totalLinks[pageNo-1]
#     response = requests.get(totalLinks)
#     #soup = BeautifulSoup(response.text,'html.parser')
#     print(response)
base_url = "https://search.shopping.naver.com/catalog/18080320568?query=%EA%B3%B5%EC%9C%A0%EA%B8%B0&NaPm=ct%3Dkh60rts8%7Cci%3D19ef7cb0202b35519f85e7de319193e447f32a0d%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D9834f25ca470b5d9e8c6aa7198d42fafcff6d4c8"
response = requests.get(base_url)
soup = BeautifulSoup(response.text,'html.parser')
o_content = soup.select("#section_review > div.filter_sort_group__Y8HA1 > div.filter_evaluation_tap__-45pp > ul > li.filter_on__X0_Fb > a > em")
fi_content = soup.select("#section_review > div.filter_sort_group__Y8HA1 > div.filter_evaluation_tap__-45pp > ul > li:nth-child(2) > a > em")
fo_content = soup.select("#section_review > div.filter_sort_group__Y8HA1 > div.filter_evaluation_tap__-45pp > ul > li:nth-child(3) > a > em")

text_content = soup.select("#section_review > ul > div.reviewItems_review__1eF8A")
overallResult = []
fiveResult = []
fourResult = []
text = []
for tag in o_content:

    em = tag.select('em')
    for extract_tag in em:
        extract_tag.extract()

    span = tag.select('span')
    for extract_tag in span:
        extract_tag.extract()

    overallResult.append(tag.getText().strip())
for tag in fi_content:

    em = tag.select('em')
    for extract_tag in em:
        extract_tag.extract()

    span = tag.select('span')
    for extract_tag in span:
        extract_tag.extract()

    fiveResult.append(tag.getText().strip())
for tag in fo_content:

    em = tag.select('em')
    for extract_tag in em:
        extract_tag.extract()

    span = tag.select('span')
    for extract_tag in span:
        extract_tag.extract()

    fourResult.append(tag.getText().strip())
# for tag in text_content:
#
#     em = tag.select('em')
#     for extract_tag in em:
#         extract_tag.extract()
#
#     span = tag.select('span')
#     for extract_tag in span:
#         extract_tag.extract()
#
#     text.append(tag.getText().strip())

print(overallResult)
print(fiveResult)
print(fourResult)
