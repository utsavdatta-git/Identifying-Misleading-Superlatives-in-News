import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

# initialize the set of links (unique links)
internal_urls = set()
external_urls = set()
total_urls_visited = 0


def is_valid(in_url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(in_url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_website_links(in_url):
    """
    Returns all URLs that is found on `url` in which it belongs to the same website
    """
    # all URLs of `url`
    urls = set()
    # domain name of the URL without the protocol
    domain_name = urlparse(in_url).netloc
    try:
        soup = BeautifulSoup(requests.get(in_url).content, "html.parser")
    except:
        soup = None
    if soup:
        for a_tag in soup.findAll("a"):
            href = a_tag.attrs.get("href")
            if href == "" or href is None:
                # href empty tag
                continue
            # join the URL if it's relative (not absolute link)
            href = urljoin(in_url, href)
            parsed_href = urlparse(href)
            # remove URL GET parameters, URL fragments, etc.
            href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
            if not is_valid(href):
                # not a valid URL
                continue
            if href in internal_urls:
                # already in the set
                continue
            if domain_name not in href:
                # external link
                if href not in external_urls:
                    external_urls.add(href)
                continue
            urls.add(href)
            internal_urls.add(href)
    return urls


def crawl(in_url, in_max_urls=30):
    """
    Crawls a web page and extracts all links.
    You'll find all links in `external_urls` and `internal_urls` global set variables.
    params:
        max_urls (int): number of max urls to crawl, default is 30.
    """
    global total_urls_visited
    total_urls_visited += 1
    links = get_all_website_links(in_url)
    for link in links:
        if total_urls_visited > in_max_urls:
            break
        crawl(link, in_max_urls=in_max_urls)
    return internal_urls


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Link Extractor Tool with Python")
    parser.add_argument("url", help="The URL to extract links from.")
    parser.add_argument("-m", "--max-urls", help="Number of max URLs to crawl, default is 30.", default=30, type=int)

    args = parser.parse_args()
    url = args.url
    max_urls = args.max_urls

    crawl(url, max_urls)
