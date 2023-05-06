import os
import requests
import argparse
from bs4 import BeautifulSoup


def spider(parser):
    s = requests.Session()
    resp = s.get(parser.url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    # links = soup.a
    # soon = links.next_sibling.next_sibling.next_sibling.next_sibling
    # print(soon)
    # for l in links:
    #     l['href']
    # for p in link.parents:
    #     print(p.name)
    imgs = soup.find_all('img', recursive=parser.r)
    url_imgs = set()
    i = 0
    for s in imgs:
        url_imgs.add(s['src'])
    for img in url_imgs:
        if 'http' not in img:
            img = parser.url + img
        download_img(img, parser.p)


def download_img(url, path):
    resp = requests.get(url, stream=True)
    name = url.split('/')[-1]
    ext = name.split('.')[-1]
    if ext in ['jpg', 'jpeg', 'png', 'gif', 'bmp']:
        file = os.path.join(path, name)
        if resp.status_code == 200:
            with open(file, mode='x') as f:
                with open(file, mode='wb') as f:
                    f.write(resp.content)
                    f.close()



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    parser.add_argument('-p', default='./data/')
    parser.add_argument('-r', action='store_true')
    parser = parser.parse_args()
    if not os.path.exists(parser.p):
        os.mkdir(parser.p)
    spider(parser)
