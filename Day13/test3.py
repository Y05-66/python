from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import time

pages = set()  # 存储已访问的页面，避免重复访问
random.seed(datetime.datetime.now().timestamp())  # 使用时间戳作为随机种子

def getInternalLinks(bsObj, includeUrl):
    """获取所有内部链接"""
    internalLinks = []
    for link in bsObj.find_all("a", href=re.compile("^(/|.*" + includeUrl + ")")):
        if link.has_attr('href'):
            href = link.attrs['href']
            if href not in internalLinks:
                internalLinks.append(href)
    return internalLinks

def getExternalLinks(bsObj, excludeUrl):
    """获取所有外部链接"""
    externalLinks = []
    for link in bsObj.find_all("a", href=re.compile("^(http|www)((?!" + excludeUrl + ").)*$")):
        if link.has_attr('href'):
            href = link.attrs['href']
            if href not in externalLinks:
                externalLinks.append(href)
    return externalLinks

def splitAddress(address):
    """分割URL地址，提取域名"""
    address = address.replace("http://", "").replace("https://", "")
    return address.split("/")[0]

def getRandomExternalLink(startingPage):
    """获取一个随机外部链接，如果没有则递归查找内部链接"""
    try:
        html = urlopen(startingPage)
        bsObj = BeautifulSoup(html, 'html.parser')
    except Exception as e:
        print(f"Error opening {startingPage}: {e}")
        return None

    domain = splitAddress(startingPage)
    externalLinks = getExternalLinks(bsObj, domain)

    if not externalLinks:  # 如果没有外部链接，尝试内部链接
        print("No external links, looking through internal links...")
        internalLinks = getInternalLinks(bsObj, domain)
        if not internalLinks:
            print("No internal links left to follow.")
            return None
        # 随机选择一个内部链接
        internalLink = random.choice(internalLinks)
        if internalLink.startswith('/'):
            internalLink = f"http://{domain}{internalLink}"
        print(f"Following internal link: {internalLink}")
        time.sleep(1)  # 避免请求过快
        return getRandomExternalLink(internalLink)
    else:
        return random.choice(externalLinks)  # 随机返回一个外部链接

def followExternalOnly(startingSite):
    """递归爬取外部链接"""
    externalLink = getRandomExternalLink(startingSite)
    if externalLink:
        print(f"Random external link is: {externalLink}")
        time.sleep(1)  # 避免请求过快
        followExternalOnly(externalLink)
    else:
        print("No more external links to follow.")

# 开始爬取
followExternalOnly("http://oreilly.com")