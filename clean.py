import argparse
import json
import codecs
import os
import itertools
from collections import defaultdict

def build_reverse_dict(aliases):
	reverse_aliases = defaultdict(lambda: {})
	for date, a in dict.iteritems(aliases):
		reverse_aliases[date] = {}
		for name, alias_list in dict.iteritems(a):
			for item in alias_list:
				reverse_aliases[date][item] = name
	return reverse_aliases

def main(datadir):
	aliases = json.load(open('aliases.json'))
	reverse_aliases = build_reverse_dict(aliases)
	for filename in os.listdir(datadir):
		year = filename.split('_')[0]
		year_aliases = reverse_aliases[year]
		f = open(datadir + '/' + filename, 'r')
		data = json.load(f)
		f.close()
		cleandata = {}
		for k, v in dict.iteritems(data):
			if k in year_aliases.keys():
				new_name = year_aliases[k]
				if new_name in cleandata:
					for date, text in dict.iteritems(v):
						cleandata[new_name][date] += text
				else:
					cleandata[new_name] = defaultdict(lambda: [], v)
		newf = open(datadir + '/' + filename, 'w')
		newf.write(json.dumps(cleandata))
    	newf.close()

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("datadir", help="directory where dataset is located", type=str)
	args = parser.parse_args()

	main(args.datadir)