import codecs
import json
from collections import defaultdict

newf = codecs.open('full_parsed_sentences.json' , 'r', encoding='utf-8')
f = json.load(newf)

def find_anaphora_epistrophe():
	aedict = defaultdict(lambda: [0,0])
	count = 0
	for candidates, dates in f.iteritems():
		length = 0
		acount = 0
		ecount = 0
		for date, speech in dates.iteritems():
			anaphora_list = []
			epistrophe_list = []
			length += len(speech)
			for sentence in speech:
				new_anaphora_list = [sentence[0:1], sentence[0:2], sentence[0:3], sentence[0:4]]
				new_epistrophe_list = [sentence[-1:], sentence[-2:], sentence[-3:], sentence[-4:]]
				amatches = 0
				ematches = 0
				if anaphora_list:
					amatches = sum([True if mini_sent == new_anaphora_list[i] else False for i, mini_sent in enumerate(anaphora_list)])
				if epistrophe_list:
					ematches = sum([True if mini_sent == new_epistrophe_list[i] else False for i, mini_sent in enumerate(epistrophe_list)])
				if amatches > 0:
					acount += amatches
				if ematches > 0:
					ecount += ematches
				anaphora_list = new_anaphora_list
				epistrophe_list = new_epistrophe_list
		aedict[candidates][0] += float(acount) / length if length > 0 else acount
		aedict[candidates][1] += float(ecount) / length if length > 0 else ecount
	print aedict

if __name__ == '__main__':
	find_anaphora_epistrophe()