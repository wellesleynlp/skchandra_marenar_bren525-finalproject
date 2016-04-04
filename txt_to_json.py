import argparse 
import os
import codecs
import json
import re

def update_dict(results, regex, text, date):
    """Find all matches of regex in the provided text"""
    regexp = re.compile(regex)
    people = set()
    for phrase in regexp.findall(text):
    	cleaned = re.split('[:;]', phrase)[0]
    	people.add(cleaned)
    for person in people:
    	if person not in results:
    		results[person] = {}
    	results[person][date] = []
    r = re.split(regex, text)
    for i, item in enumerate(r):
    	item_cleaned = re.split('[:;]', item)[0]
    	if item_cleaned in people:
            print item_cleaned
            results[item_cleaned][date].append(r[i+1])
    return results

def main(datadir):
	files = os.listdir(datadir)
	results = {}
	for filename in files: 
		f = codecs.open(datadir + "/" + filename, 'r', encoding='utf-8')
		text = f.read()
		date = filename.split('.')[0]
		results = update_dict(results, r'([A-Z][A-Z]*[. \n]*[A-Z]*[:;])', text, date)
	
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("datadir", help="directory where dataset is located", type=str)
	args = parser.parse_args()

	main(args.datadir)