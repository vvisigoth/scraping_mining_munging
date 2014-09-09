#! /usr/bin/env python
import sys, urllib2, json

from pprint import pprint as pretty_print

from urllib import urlencode

from bs4 import BeautifulSoup as bsoup

BASE_URL = "http://losangeles.craigslist.org/search/sss?"

USER_AGENT_STRING = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 Safari/537.36"

def make_url(query_term):

    params = {
        "query": query_term
    }

    param_string = urlencode(params)

    return BASE_URL + param_string


def send_request(url, user_agent_string):

    headers = { 'User-Agent' : user_agent_string}

    req = urllib2.Request(url, None, headers)

    data = urllib2.urlopen(req).read()

    return data


def main():

    url = make_url("Dining Room Chairs")

    html = send_request(url, USER_AGENT_STRING)

    return html
 
if __name__ == '__main__':
    pretty_print(main())
