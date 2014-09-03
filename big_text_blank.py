#! /usr/bin/env python
import sys, re
from urllib2 import urlopen as open_url

TEXT_URL = 'http://norvig.com/big.txt'

def get_text(url):
    """Takes a url and returns response in text form """

    response = open_url(url)

    print response.code
    print response.headers

    return response.read()

def clean_text(text):
    """Clean text of superfluous newline characters"""

    #TIP: Using regular expressions will make life easier/better!

    #EXTRA Also strip out punctuation

    #CODE HERE

    return clean_text



def count_words(text, count):
    """Takes a string of text and count dict returns updated count dict"""

    #CODE HERE

    return updated_count



def count_word(word, count):

    """Take a word, update the count dict"""

    #EXTRA Make the count case insensitive, ie "Bed" and "bed" should count

    return updated_count_dict

def sort_dict(count):
    """convert a dict to a list sorted by value"""

    #TIP: Google 'sorting python dictionary by value'

    #CODE HERE

    return sorted_list

def main():
    """Main function"""
    # BASIC: Take a url of a text document and return a dictionary of word occurrences
    # EXTRA: Return a sorted list (descending) of word occurrences
    # EXTRA: Return a list of sentences that include a given keyword, which should be commandline argument

    return word_count
 
if __name__ == '__main__':
    print main()
