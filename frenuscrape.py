# -*- coding: utf-8 -*-

from lxml import html
import requests

baseurl = "x"

for x in range(0, 1):
    url = baseurl
    page = requests.get(url)
    tree = html.fromstring(page.content)

    imgur = tree.xpath('//a/@href[starts-with(., "x/thread/")]')

    for x in imgur:
        url = x
        page = requests.get(url)
        tree = html.fromstring(page.content)
        imgur = tree.xpath('//a/@href[starts-with(., "https://imgur.com/") or starts-with(., "http://imgur.com/")]')

        if len(imgur) > 0:
            with open("links.txt", "a") as myfile:
                myfile.write("Link: %s Site: %s  \n" % (str(url), str(imgur)))

            print(x, imgur)
