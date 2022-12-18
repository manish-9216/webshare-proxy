import requests
from random import *
import numpy as np
import requests
from bs4 import BeautifulSoup
from datetime import date



def get_proxies(key):
    res = requests.get("https://proxy.webshare.io/api/proxy/list/", headers={"Authorization": f'Token {key}'})
    proxies_list = []
    for x in res.json()["results"]:
        proxy = f'{x["username"]}:{x["password"]}@{x["proxy_address"]}:{x["ports"]["http"]}'
        proxies_list.append(proxy)

    shuffle(proxies_list)
    prox = (proxies_list[0])
    return prox


def prox_request_maker():
    proxie = get_proxies('spd7chvqldmvu8giiynk8lb7jr2ap6zo8flr332r')
    proxies = {
    "http": "http://"+proxie,
    "https": "http://"+proxie,
    }

    return proxies




def main():

    url = "https://www.hermes.com/us/en/"
    proxies = prox_request_maker()
    print(proxies)

    response = requests.get(url,proxies=proxies)
    soup = BeautifulSoup(response.content, 'html.parser')
    # prod_list_class = soup.find_all('a',{'class':'treeitem'})
    print(response)
    print(soup)
    # for a in prod_list_class:
    #     print(a.find_all('a',{'role':'treeitem'}))

    # product_urls = ["https://www.hermes.com"+i.find('a').get('href') for i in prod_list_class]

    # print(product_urls[:-13])

main()
















































# def get_proxies(key):
#     res = requests.get("https://proxy.webshare.io/api/proxy/list/", headers={"Authorization": f'Token {key}'})
#     # proxies_dict = {}
#     proxies = []
#     for x in res.json()["results"]:
#         proxy = f'{x["username"]}:{x["password"]}@{x["proxy_address"]}:{x["ports"]["http"]}'
#         proxies.append(f"http://qmhezatz:{proxy}")
#         # return proxies

#     shuffle(proxies)
#     prox = (proxies[0])

#     return prox


# proxies = get_proxies('spd7chvqldmvu8giiynk8lb7jr2ap6zo8flr332r')

