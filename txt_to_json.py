import argparse 
import os
import codecs
import json
import re

def search(regex, text):
    """Find all matches of regex in the provided text"""
    regexp = re.compile(regex)
    people = set()
    results = {}
    for phrase in regexp.findall(text):
    	people.add(phrase)
    r = re.split(regex, text)
    for i, item in enumerate(r):
    	print item
    print "boop"

def main(datadir):
	path = datadir + '/train'
	files = os.listdir(path)
	for filename in files: 
		f = codecs.open(path + "/" + filename, 'r', encoding='utf-8')
		text = f.read()
		search(r'([A-Z][A-Z]*[. \n]*[A-Z]*[:;])', text)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("datadir", help="directory where dataset is located", type=str)
	args = parser.parse_args()

	main(args.datadir)