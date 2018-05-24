# -*- coding: utf-8 -*-

from lxml import html
import requests
import shutil

baseurl = "to fill"
num = 100
counter = 0
pages = []

for n in range(1, num):
    pages.append("page-%s" % (n))

print(pages)

for topic in pages:
    page = "%s/%s" % (baseurl, topic)
    print(page)

    url = page
    page = requests.get(url)
    tree = html.fromstring(page.content)

    imgur = tree.xpath('//a/@href[starts-with(., "x/thread/")]')

    for links in imgur:
        url = links
        page = requests.get(url)
        tree = html.fromstring(page.content)
        imgurr = tree.xpath('//a/@href[starts-with(., "https://imgur.com/") or starts-with(., "http://imgur.com/")]')

        if len(imgurr) > 0:
            for image in imgurr:
                counter += 1
                url = image
                page = requests.get(url)
                tree = html.fromstring(page.content)
                imgurrr = tree.xpath('//a/@href[contains(., "i.imgur")]')

                for idx, val in enumerate(imgurrr):
                    image = "https:%s" % (val)

                    response = requests.get(image, stream=True)
                    print(response)

                    with open('images/output_%s_%s.jpg' % (idx, counter), 'wb') as handle:
                        for block in response.iter_content(1024):
                            handle.write(block)

            # with open("links.txt", "a") as myfile:
                # myfile.write("Link: %s \n \n Imgur: %s  \n \n \n \n \n" % (str(url), str(imgur)))

            # print(x, imgur)
