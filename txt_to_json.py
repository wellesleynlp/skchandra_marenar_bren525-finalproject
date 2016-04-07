import argparse 
import os
import codecs
import json
import re
from collections import defaultdict

def update_dict(results, regex, text, date):
    """Find all matches of regex in the provided text"""
    regexp = re.compile(regex)
    people = set()
    for phrase in regexp.findall(text):
    	people.add(phrase)
    for person in people:
        cleaned = re.split('[:;]', person.split('\n')[1])[0]
    	results[cleaned][date] = []
    r = re.split(regex, text) 
    for i, item in enumerate(r):
    	if item in people:
            item_cleaned = re.split('[:;]', item.split('\n')[1])[0]
            results[item_cleaned][date].append(r[i+1])
    return results


def main(datadir):
    results = defaultdict(lambda: {})
    for filename in os.listdir(datadir): 
        f = codecs.open(datadir + "/" + filename, 'r', encoding='utf-8')
        text = f.read()
        date = filename.split('.')[0]
        results = update_dict(results, r'(\nM[RSrs]{1,2}\. [A-Z][\w\']*[\.:;]|[\n][A-Z]*[,-. ]*[A-Z]*[,-. ]*[A-Z]*[,-. ]*[A-Z]*[,-. ]*[A-Z]*[,-. ]*[A-Z]*[,-. ]*[A-Z]*[,-. ]*[:]|[\n][A-Z][a-z]*[.][ ]\w*[,-. ]*\w*[,-. ]*\w*[,-. ]\w*[,-. ]*\w*[,-. ]*\w*[,-. ]\w*[,-. ]*[:]|[\n][A-Z]*[a-z]*[A-Z]*[:]|[\n][A-Z]*[:;]|[\n][A-Z]\w*[:;]|[\n][A-Z]*[. ]*[A-Z]*[ ]*[A-Z]*[ ,(]*[A-Z]*[a-z]*[-,]*[A-Z]*[a-z]*[) ]*[A-Z]*[ ]*[A-Z]*[:]|\nThe President\.|\nTHE PRESIDENT\.|\nTHE MODERATOR\.|\nSenator [A-Z][a-z]*\.|\nGovernor [A-Z][a-z]*\.|\nGOVERNOR [A-Z]*\.|\nPresident [A-Z][a-z]*\.|\nSenator John F\. Kerry\.|\nFormer \w*[. ]*\w*[. ]*\w[. ]*\w*[. ]*\w*[. ]*\w*[. ]*\w*[. ]*\w*[. ]*[:]|\nFormer Virginia Governor James Gilmore \(R\-Va\.\)\:|\nO\'Brien[:;]|[\n][A-Z][a-z]*[ ]*[A-Z][a-z]*[ ]*[A-Z][a-z]*[ (]*[A-Z]*[-]*[A-Z]*[a-z]*[). ]*[:])', text, date)
    print results.keys()
    year = datadir.split('/')[0]
    debate = datadir.split('/')[1]
    new_file = open('data/' + year + '_' + debate + '.json', "w")
    new_file.write(json.dumps(results))
    new_file.close()

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("datadir", help="directory where dataset is located", type=str)
	args = parser.parse_args()

	main(args.datadir)