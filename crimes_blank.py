#! /usr/bin/env python
import sys, urllib2, json

from pprint import pprint as pretty_print

from urllib import urlencode

SAMPLE_URL = ""

USER_AGENT_STRING = ""

def make_url(date_begin, date_end, address, crime_codes):
    pass


def get_crimes(url, user_agent_string):

    headers = { 'User-Agent' : user_agent_string}

    req = urllib2.Request(url, None, headers)

    data = urllib2.urlopen(req).read()

    return json.loads(data)

def main():

    return get_crimes(BASE_URL, USER_AGENT_STRING)
 
if __name__ == '__main__':
    pretty_print(main())
