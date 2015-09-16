#!/usr/bin/python3
import os
from urllib.request import urlopen, urlretrieve
import uuid
from html.parser import HTMLParser
import argparse


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__(self)
        self.file_link_dict = dict()

    def handle_starttag(self, tag, attrs):
        # print("tag %r \n attrs %r" % (tag, attrs))
        title = ('title', 'Download')
        if tag == "a":
            if title in attrs:
                for attr_name, attr_value in attrs:
                    if attr_name == 'href':
                        self.file_link_dict["%s.torrent" % str(uuid.uuid4())] = attr_value
                        print(attr_value)

    def get_link_dict(self):
        return self.file_link_dict


def download_file(file_link_dict, destination):
    """ Take a list and download items then run each downloaded file
    """
    for key, link in file_link_dict.items():
        fname = os.path.join(destination, key)
        urlretrieve(link, fname)

def main(url, destination):
    request = urlopen(url)
    html_text = str(request.readlines())
    html_parser = MyHTMLParser()
    file_link_dict = html_parser.feed(html_text)
    download_file(html_parser.get_link_dict(), destination)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="Url on nyaa.se")
    parser.add_argument("destination", help="Torrent files destination")
    args = parser.parse_args()
    main(args.url, args.destination)














