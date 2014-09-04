#! /usr/bin/env python
import sys, urllib2, json

from pprint import pprint as pretty_print

from urllib import urlencode

#THIS PART OF THE URL WILL NOT CHANGE
BASE_URL = "http://www.crimemapping.com/GetIncidents.aspx"

#WE NEED A STRING TO IDENTIFY OUR LIL' BOT TO
#THE SERVER
USER_AGENT_STRING = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 Safari/537.36"


#THIS FUNCTION WILL OUTPUT A PRETTY LITTLE URL
def make_url(date_begin, date_end, address, crime_codes):

    #JOIN IS THE OPPOSITE OF SPLIT, IT TURNS A LIST
    #INTO STRING
    crime_code_string = ','.join(crime_codes) 

    #MAKE A DICTIONARY OF THE THE URL PARAMETERS
    params = { 
        'ccs': crime_code_string,
        'add': address,
        'bcy': 4035817.0474122106,
        'bcx': -13162826.191908287,
        'br': 1.0,
        'xmin': -13169676.86056835,
        'ymin': 4032941.3504065443,
        'xmax': -13155975.52324825,
        'ymax': 4038693.2367849965
        }

    #DATES NEED TO BE FORMATTED DIFFERENTLY

    #'URLENCODE' TAKES A DICT AND TURNS IT INTO A STRING
    param_string = urlencode(params)

    return BASE_URL + '?' + param_string + '&db=' + date_begin + '&de=' + date_end


#THIS FUNCTION GOES TO THE SERVER AND GETS THE DATA
def get_crimes(url, user_agent_string):

    #HEADERS IN A DICT
    headers = { 'User-Agent' : user_agent_string}

    #SEND OFF REQUEST
    req = urllib2.Request(url, None, headers)

    #READ RESPONSE INTO THE VARIABLE 'data'
    data = urllib2.urlopen(req).read()

    #THE RESPONSE IS IN THE JSON FORMAT
    return json.loads(data)

def main():

    #GET ASSAULT DATA
    url = make_url('8/29/2014+00:00:00', '9/04/2014+23:59:00', 'Los Angeles, California', ['AS'])

    return get_crimes(url, USER_AGENT_STRING)
 
if __name__ == '__main__':
    pretty_print(main())
