import getUrls
from bs4 import BeautifulSoup
import requests
import colorama
import pandas as pd


def write_dict_to_csv(in_dict):
    """Writes dictionary data to excel

            Attributes
            ----------
            in_dict : dictionary
                dictionary with scraped data with labels
    """
    # Convert incoming dict to dataframe
    new_dataframe = pd.DataFrame.from_dict(in_dict)
    # Read existing csv file to a dataframe
    try:
        existing_file = pd.read_excel("news_dataset.xlsx", engine="openpyxl")
        new_dataframe = pd.concat([existing_file, new_dataframe], ignore_index=True)
        new_dataframe.to_excel("news_dataset.xlsx", index=False, engine="openpyxl")
    except:
        new_dataframe.to_excel("news_dataset.xlsx", index=False, engine="openpyxl")


def scrape_and_label_data(in_parent_url):
    """Recursively scrapes headlines and bodies of news articles based on the parent url and then asks for their labels

            Attributes
            ----------
            in_parent_url : string
                url if the site to be scraped
    """
    GREEN = colorama.Fore.GREEN
    RESET = colorama.Fore.RESET
    YELLOW = colorama.Fore.YELLOW

    # Define all lists
    all_headlines = []
    all_bodies = []
    misleading = []
    dataframe_dict = {}
    news_item_count = 0
    all_urls = getUrls.crawl(in_parent_url, 500)

    for url in all_urls:
        try:
            soup = BeautifulSoup(requests.get(url).content, "html.parser")
        except:
            soup = None
        if soup:
            headings = soup.findAll("h1")
            for heading in headings:
                if 10 <= len(heading.text.strip().split()) <= 25:
                    bodies = soup.findAll('p')
                    for body in bodies:
                        if 30 <= len(body.text.strip().split()) <= 200 and (heading.text.strip().find("सबसे") >= 0 or
                                                                            heading.text.strip().find("सर्वाधिक") >= 0):
                            print(f"{GREEN}[HEADLINE]: {heading.text}{RESET}")
                            print(f"{YELLOW}[BODY]: {body.text}{RESET}")
                            ignore = input("Ignore? (Y/N): ")
                            if ignore == "N":
                                news_item_count += 1
                                mislead = input("Mislead (Y(1)/N(0)?: ")
                                misleading.append(mislead)
                                all_headlines.append(heading.text)
                                all_bodies.append(body.text)
                                if news_item_count == 50:
                                    dataframe_dict["Headline"] = all_headlines
                                    dataframe_dict["Body"] = all_bodies
                                    dataframe_dict["Misleading"] = misleading
                                    write_dict_to_csv(dataframe_dict)
                                    news_item_count = 0
                                    all_headlines = []
                                    all_bodies = []
                                    misleading = []
                                    dataframe_dict = {}


scrape_and_label_data("https://ndtv.in//#pfrom=ndtv-globalnav")
