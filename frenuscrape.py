# -*- coding: utf-8 -*-

from lxml import html
import requests

baseurl = "x"
num = 100
pages = []

for n in range(1, num):
    pages.append("page-%s" % (n))

print(pages)

for z in pages:
    page = "%s/%s" % (baseurl, z)
    print(page)

    url = page
    page = requests.get(url)
    tree = html.fromstring(page.content)

    imgur = tree.xpath('//a/@href[starts-with(., "x/thread/") and contains(., "x")]')

    for x in imgur:
        url = x
        page = requests.get(url)
        tree = html.fromstring(page.content)
        imgur = tree.xpath('//a/@href[starts-with(., "https://imgur.com/") or starts-with(., "http://imgur.com/")]')

        if len(imgur) > 0:
            with open("links.txt", "a") as myfile:
                myfile.write("Link: %s \n \n Imgur: %s  \n \n \n \n \n" % (str(url), str(imgur)))

            print(x, imgur)
