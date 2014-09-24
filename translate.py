#!/usr/bin/env python3
# translate.py

import sys, argparse
import requests
from bs4 import BeautifulSoup

#if __name__=='__main__':

parser = argparse.ArgumentParser()
parser.add_argument(
	'from_lang', metavar='STR', type=str, help='language to be translated from. example: en, fr, etc.')
parser.add_argument(
	'to lang', metavar='STR', type=str, help='language to be translated to')
parser.add_argument(
	'text', metavar='STR', nargs='+', type=str, help='text to be translated')

args = parser.parse_args()

def translate(from_lang, to_lang, text):
	payload = {'sl' : from_lang, 'tl' : to_lang, 'js' : 'n', 'text' : text}
	response_text = requests.post('https://translate.google.com/',data=payload).text
	return BeautifulSoup(response_text).find(id='result_box').find('span').text

print(translate(sys.argv[1], sys.argv[2], ' '.join(sys.argv[3:])))


