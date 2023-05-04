import sys
import os
import requests
from bs4 import BeautifulSoup

def p_save_in_path():
    dir = None
    if not dir == None:
        dir = os.mkdir('./data')

def spider():
    
    s = requests.Session()
    resp = s.get(sys.argv[2])
    soup = BeautifulSoup(resp.text, 'html.parser').find_all('img')
    for s in soup:
        print(s['src'])



if __name__ == '__main__':
    spider()

