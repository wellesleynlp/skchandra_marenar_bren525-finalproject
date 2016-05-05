import argparse
import json
import codecs
import os
import itertools
from collections import defaultdict
from nltk import word_tokenize, sent_tokenize
from string import punctuation

def main(datadir):
	megadict = defaultdict(lambda: {})
	for filename in os.listdir(datadir):
		split_name = filename.split('_')
		year = split_name[0]
		election_type = split_name[1].split('.')[0]
		f = codecs.open(datadir + '/' + filename, 'r', encoding='utf-8')
		data = json.load(f)
		f.close()
		for name, v in dict.iteritems(data):
			for date, text in dict.iteritems(v):
				sentences = sent_tokenize("".join(text))
				text = ''.join(sentences)
				election_name = name + " " + election_type + " " + year
				if election_name != "Hillary Clinton republican 2008":
					megadict[election_name][date] = text
	newf = codecs.open('full_text.json' , 'w', encoding='utf-8')
	newf.write(json.dumps(megadict))
	newf.close()

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("datadir", help="directory where dataset is located", type=str)
	args = parser.parse_args()

	main(args.datadir)

	#([A-Za-z ]*\.){1,3} ?(?=\[Laughter\])