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

    #EXTRA Also strip out punctuation

    return re.sub('\n+', ' ', text)

def count_words(text, count):
    """Takes a string of text and count dict returns updated count dict"""

    split_words = text.split(' ')

    for word in split_words:

        count = count_word(word, count)

    return count

def sort_dict(count):
    """convert a dict to a list sorted by value"""
    pass

def count_word(word, count):

    """Take a word, update the count dict"""

    #EXTRA Make the count case insensitive, ie "Bed" and "bed" should count

    if (count.get(word)):
        count[word] = count[word] + 1
    else:
        count[word] = 1

    return count

def main():
    """Main function"""
    # BASIC: Take a url of a text document and return a dictionary of word occurrences
    # EXTRA: Return a sorted list (descending) of word occurrences
    # EXTRA: Return a list of sentences that include a given keyword, which should be commandline argument

    empty_count = {}

    print count_words(clean_text(get_text(TEXT_URL)), empty_count) 
 
if __name__ == '__main__':
    main()
