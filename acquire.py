import requests
from bs4 import BeautifulSoup 
import pandas as pd
import re
from time import strftime
from time import sleep
import os
import json
from typing import Dict, List, Optional, Union, cast

from env import github_token, github_username



def get_url_list():
    '''
    Gets a list of urls from the github star ranking page, iterating through the different pages and grabbing,
    each url from the different github repositories.
    '''
    # Created an empty list that will hold all of the github links from each page.
    link_list = []
    # Created a for loop in order to get different pages for the p = {i}
    for i in range(1,99):
        # When 10 pages are accessed by the web scraper this is here to take a minute break to avoid,
        # having github throtal the webscrape.
        if i%10 == 0:
            # prints a different link in the link list to show that the pulls are working correctly
            print(link_list[i*2])
            # Prints the length of the link list to show that the list is growing correctly
            print(len(link_list))
            # shows that the sleep function is about to start and will pause function for 60 seconds
            print('waiting')
            sleep(60)
            # shows that the sleep is over
            print('continue')
            # Creates a response basically pulling in https://github.com/search?p=&q=stars%3A%3E0&s=stars&type=Repositories this link 99 times
            response = requests.get(f'https://github.com/search?p=100{i}&q=stars%3A%3E0&s=stars&type=Repositories',headers = {'user-agent': 'Codeup DS Germain'})
            # gets the text version to prepare it for beautiful soup
            html = response.text
            # use beautiful soup on the html
            soup = BeautifulSoup(html)
            # pulls the target html which holds the link of each github on that page
            text_with_link = soup.select('.v-align-middle')
            # iterates through each peice of html and will check if the regex below matches with anything.
            for link in text_with_link:
                # turning the html to a string
                link_ispy = str(link)
                # setting all the links to match
                match = re.search(r'(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-]\w+)', link_ispy)
                # checks if match is null and only passes through non null values
                if match is not None:
                    # appends the link to the link list
                    link_list.append(match.group(0))
        else:
            # Creates a response basically pulling in https://github.com/search?p=&q=stars%3A%3E0&s=stars&type=Repositories this link 99 times
            response = requests.get(f'https://github.com/search?p={i}&q=stars%3A%3E0&s=stars&type=Repositories',headers = {'user-agent': 'Codeup DS Germain'})
            # gets the text version to prepare it for beautiful soup
            html = response.text
            # use beautiful soup on the html
            soup = BeautifulSoup(html)
            # pulls the target html which holds the link of each github on that page
            text_with_link = soup.select('.v-align-middle')
            # iterates through each peice of html and will check if the regex below matches with anything.
            for link in text_with_link:
                # turning the html to a string
                link_ispy = str(link)
                # setting all the links to match
                match = re.search(r'(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-]\w+)', link_ispy)
                # checks if match is null and only passes through non null values
                if match is not None:
                    link_list.append(match.group(0))
    return link_list

headers = {"Authorization": f"token {github_token}", "User-Agent": github_username}

if headers["Authorization"] == "token " or headers["User-Agent"] == "":
    raise Exception(
        "You need to follow the instructions marked TODO in this script before trying to use it"
    )


def github_api_request(url: str) -> Union[List, Dict]:
    response = requests.get(url, headers=headers)
    response_data = response.json()
    if response.status_code != 200:
        raise Exception(
            f"Error response from github api! status code: {response.status_code}, "
            f"response: {json.dumps(response_data)}"
        )
    return response_data


def get_repo_language(repo: str) -> str:
    url = f"https://api.github.com/repos/{repo}"
    repo_info = github_api_request(url)
    if type(repo_info) is dict:
        repo_info = cast(Dict, repo_info)
        if "language" not in repo_info:
            raise Exception(
                "'language' key not round in response\n{}".format(json.dumps(repo_info))
            )
        return repo_info["language"]
    raise Exception(
        f"Expecting a dictionary response from {url}, instead got {json.dumps(repo_info)}"
    )


def get_repo_contents(repo: str) -> List[Dict[str, str]]:
    url = f"https://api.github.com/repos/{repo}/contents/"
    contents = github_api_request(url)
    if type(contents) is list:
        contents = cast(List, contents)
        return contents
    raise Exception(
        f"Expecting a list response from {url}, instead got {json.dumps(contents)}"
    )


def get_readme_download_url(files: List[Dict[str, str]]) -> str:
    """
    Takes in a response from the github api that lists the files in a repo and
    returns the url that can be used to download the repo's README file.
    """
    for file in files:
        if file["name"].lower().startswith("readme"):
            return file["download_url"]
    return ""


def process_repo(repo: str) -> Dict[str, str]:
    """
    Takes a repo name like "gocodeup/codeup-setup-script" and returns a
    dictionary with the language of the repo and the readme contents.
    """
    contents = get_repo_contents(repo)
    readme_download_url = get_readme_download_url(contents)
    if readme_download_url == "":
        readme_contents = ""
    else:
        readme_contents = requests.get(readme_download_url).text
    return {
        "repo": repo,
        "language": get_repo_language(repo),
        "readme_contents": readme_contents,
    }


def scrape_github_data() -> List[Dict[str, str]]:
    """
    Loop through all of the repos and process them. Returns the processed data.
    """
    return [process_repo(repo) for repo in REPOS]


if __name__ == "__main__":
    data = scrape_github_data()
    json.dump(data, open("data.json", "w"), indent=1)