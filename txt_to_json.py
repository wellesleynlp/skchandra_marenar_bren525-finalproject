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
    	people.add(phrase)
    for person in people:
        cleaned = re.split('[:;]', person.split('\n')[1])[0]
    	if cleaned not in results:
    		results[cleaned] = {}
    	results[cleaned][date] = []
    r = re.split(regex, text)
    for i, item in enumerate(r):
    	if item in people:
            item_cleaned = re.split('[:;]', item.split('\n')[1])[0]
            results[item_cleaned][date].append(r[i+1])
    return results

def main(datadir):
    files = os.listdir(datadir)
    results = {}
    for filename in files: 
        f = codecs.open(datadir + "/" + filename, 'r', encoding='utf-8')
        text = f.read()
        date = filename.split('.')[0]
        results = update_dict(results, r'([\n][A-Z][A-Z]*[a-z]*[. \n]*[A-Z]*[a-z]*[A-Z]*[:;])', text, date)
    print results

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("datadir", help="directory where dataset is located", type=str)
	args = parser.parse_args()

	main(args.datadir)