import argparse
import json
import codecs
import os
import itertools
from collections import defaultdict
from nltk import word_tokenize, sent_tokenize
from string import punctuation

def main(datadir):
	testing = ['2016', '1976', '1984', '1992', '2000']
	megadict = defaultdict(lambda: {})
	for filename in os.listdir(datadir):
		split_name = filename.split('_')
		year = split_name[0]
		election_type = split_name[1].split('.')[0]
		f = codecs.open(datadir + '/' + filename, 'r', encoding='utf-8')
		data = json.load(f)
		f.close()
		if year not in testing:
			for name, v in dict.iteritems(data):
				for date, text in dict.iteritems(v):
					sentences = sent_tokenize("".join(text))
					words = [word_tokenize(t) for t in sentences]
					for index, w in enumerate(words):
						words[index] = [x.lower() for x in w]
					exclude = set(punctuation)
					exclude = exclude | {"`", "--", "'", "..."}
					s = [word for sentence in words for word in sentence if word not in exclude]
					election_name = name + " " + election_type + " " + year
					if election_name != "Hillary Clinton republican 2008":
						megadict[election_name][date] = s
	newf = codecs.open('parsed.json' , 'w', encoding='utf-8')
	newf.write(json.dumps(megadict))
	newf.close()

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("datadir", help="directory where dataset is located", type=str)
	args = parser.parse_args()

	main(args.datadir)