import os
import requests
import argparse
from bs4 import BeautifulSoup
import time


def spider(parser):
    deepth_level(parser.url, parser.l, parser.p)
    # s = requests.Session()
    # resp = s.get(parser.url)
    # soup = BeautifulSoup(resp.text, 'html.parser')
    # tags = soup('a')
    # len_url = len(parser.url)
    # for link in tags:
    #     l = link.get('href')
    #     if l == None:
    #         continue
    #     if l[0] == '/':
    #         l = parser.url + l[1:]
    #     elif l[:len_url] != parser.url:
    #         continue
    #     print(l)
    # imgs = soup.find_all('img', recursive=parser.r)
    # url_imgs = set()
    # for s in imgs:
    #     url_imgs.add(s['src'])
    # ### start = time.time()
    # ### download_imgs(url_imgs, parser.p, parser.url)
    # for img in url_imgs:
    #     if img[:4] != 'http':
    #         img = parser.url + img
    #     download_img(img, parser.p)
    ### end = time.time()
    ### print("The time of execution is: ", (end-start) * 10**3, "ms")


def deepth_level(url, level, path):
    i = 1
    s = requests.Session()
    resp = s.get(parser.url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    tags = soup('a')
    len_url = len(parser.url)
    set_urls = set()
    for link in tags:
        link = link.get('href')
        if link[0] == '/':
            link = link.split('/')[1]
            link = parser.url + link
        elif link[:len_url] != parser.url:
            continue
        set_urls.add(link)
    for l in set_urls:
        if i < level:
            deepth_level(l, level - 1, path)
            print(l)
            # download_img(l, path)
        else:
            continue


def download_img(url, path):
    resp = requests.get(url, stream=True)
    if resp.status_code == 200:
        name = url.split('/')[-1]
        ext = name.split('.')[-1]
        if ext in ['jpg', 'jpeg', 'png', 'gif', 'bmp']:
            file = os.path.join(path, name)
            try:
                fn = open(file, mode='x')
                fn.close()
            except FileExistsError:
                pass
            finally:
                with open(file, mode='wb') as f:
                    f.write(resp.content)            
                


def download_imgs(urls, path, origin):
    i = 0
    for url in urls:
        if url[:4] != 'http':
            url = origin + url
        resp = requests.get(url, stream=True)
        if resp.status_code == 200:
            ext = url.split('.')[-1]
            if ext in ['jpg', 'jpeg', 'png', 'gif', 'bmp']:
                file = os.path.join(path, 'img' + str(i) + '.' + ext)
                try:
                    fn = open(file, mode='x')
                    fn.close()
                except FileExistsError:
                    pass
                finally:
                    with open(file, mode='wb') as f:
                        f.write(resp.content)       
                i += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    parser.add_argument('-p', default='./data/')
    parser.add_argument('-r', action='store_true')
    parser.add_argument('-l', default=5, type=int)
    parser = parser.parse_args()
    if not os.path.exists(parser.p):
        os.mkdir(parser.p)
    spider(parser)
