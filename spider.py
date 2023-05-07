import os
import requests
import argparse
from bs4 import BeautifulSoup
import time


def spider(parser):
    s = requests.Session()
    resp = s.get(parser.url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    # tags = soup('a')
    # for link in tags:
    #     print(link.contents[0], link.get('href'))
    imgs = soup.find_all('img', recursive=parser.r)
    url_imgs = set()
    for s in imgs:
        url_imgs.add(s['src'])
    ### start = time.time()
    ### download_imgs(url_imgs, parser.p, parser.url)
    for img in url_imgs:
        if img[:4] != 'http':
            img = parser.url + img
        download_img(img, parser.p)
    ### end = time.time()
    ### print("The time of execution is: ", (end-start) * 10**3, "ms")


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
    parser = parser.parse_args()
    if not os.path.exists(parser.p):
        os.mkdir(parser.p)
    spider(parser)
