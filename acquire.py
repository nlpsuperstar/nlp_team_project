import requests
from bs4 import BeautifulSoup 
import pandas as pd
import re
from time import strftime
from time import sleep



def get_url_list():
    # Created an empty list that will hold all of the github links from each page.
    link_list = []
    for i in range(1,99):
        if i%10 == 0:
            print(link_list[i-3])
            print(len(link_list))
            print('waiting')
            sleep(60)
            print('continue')
            response = requests.get(f'https://github.com/search?p=100{i}&q=stars%3A%3E0&s=stars&type=Repositories',headers = {'user-agent': 'Codeup DS Germain'})
            html = response.text
            html
            soup = BeautifulSoup(html)
            article = soup.select('.v-align-middle')
            for a in article:
                link_ispy = str(a)
                match = re.search(r'(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-]\w+)', link_ispy)
                if match is not None:
                    link_list.append(match.group(0))
        else:
            response = requests.get(f'https://github.com/search?p={i}&q=stars%3A%3E0&s=stars&type=Repositories',headers = {'user-agent': 'Codeup DS Germain'})
            html = response.text
            html
            soup = BeautifulSoup(html)
            article = soup.select('.v-align-middle')
            for a in article:
                link_ispy = str(a)
                match = re.search(r'(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-]\w+)', link_ispy)
                if match is not None:
                    link_list.append(match.group(0))
    return link_list