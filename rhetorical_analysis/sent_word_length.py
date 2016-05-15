import codecs
import json
from nltk import sent_tokenize, word_tokenize
from collections import defaultdict

newf = codecs.open('../clean_data_formats/full_text.json' , 'r', encoding='utf-8')
f = json.load(newf)

avg_length = defaultdict(list)

for candidate, dates in f.iteritems():
	sent_length = 0
	sent_count = 0
	word_length = 0
	word_count = 0

	for date,speech in dates.iteritems():
		if len(speech) != 0:
			for sent in speech:
				words = word_tokenize(sent)
				sent_length += len(words)
				sent_count += 1

				for word in words:
					word_length += len(word)
					word_count += 1
		
	if sent_count != 0:
		s = sent_length / sent_count
		w = word_length / word_count
		print s,w
		avg_length[candidate] = [s,w]

length = codecs.open('avg_length.json' , 'w', encoding='utf-8')
length.write(json.dumps(avg_length))
length.close()

print avg_length