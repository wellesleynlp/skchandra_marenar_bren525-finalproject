import os
import codecs
import json
import re
import indicoio
from collections import defaultdict
indicoio.config.api_key = '83ee5c7e4241e14b4b21d3a9f31fca8c'

newf = codecs.open('full_text.json' , 'r', encoding='utf-8')
f = json.load(newf)

def search(regex,text):
    """Find all matches of regex in the provided text"""
    regexp = re.compile(regex)
    results = list()
    for phrase in regexp.findall(text):
        results.append(phrase)
    #return ' '.join(results)
    return results

laughter = defaultdict(list)
applause = defaultdict(list)

for candidate,dates in f.iteritems():
	for date,speech in dates.iteritems():
		r = {}
		r[1] = search(r'([\w|\'|\-|\, ]*\.){1,3} ?(?=\[Applause\])',speech)
		r[2] = search(r'([\w|\'|\-|\, ]*\.){1,3} ?(?=\[applause\])',speech)
		r[3] = search(r'([\w|\'|\-|\, ]*\.){1,3} ?(?=\(Applause\))',speech)
		r[4] = search(r'([\w|\'|\-|\, ]*\.){1,3} ?(?=\(applause\))',speech)

		r[5] = search(r'([\w|\'|\-|\, ]*\.){1,3} ?(?=\[Laughter\])',speech)
		r[6] = search(r'([\w|\'|\-|\, ]*\.){1,3} ?(?=\[laughter\])',speech)
		r[7] = search(r'([\w|\'|\-|\, ]*\.){1,3} ?(?=\(Laughter\))',speech)
		r[8] = search(r'([\w|\'|\-|\, ]*\.){1,3} ?(?=\(laughter\))',speech)
		
		for key,val in r.iteritems():
			if val:
				words = [sent.split(' ') for sent in val]
				if key < 5:
					applause[candidate].append(words)
				else:
					laughter[candidate].append(words)

		# applause[candidate].append(r1).append(r2).append(r3).append(r4)
		# laughter[candidate].append(r5).append(r6).append(r7).append(r8)
	# applause[candidate] = applause[candidate]/float(len(dates))
	# laughter[candidate] = laughter[candidate]/float(len(dates))
	print 'finished',candidate

#laughter_keywords = {}
#applause_keywords = {}

# for candidate,speech in laughter.iteritems():
# 	if speech:
# 		laughter_keywords[candidate] = sorted(indicoio.keywords(speech, version=2))

# for candidate,speech in applause.iteritems():
# 	if speech:
# 		applause_keywords[candidate] = sorted(indicoio.keywords(speech, version=2))

# laugh = codecs.open('laughter_count.json' , 'w', encoding='utf-8')
# laugh.write(json.dumps(laughter))
# laugh.close()

laugh_key = codecs.open('laughter_keywords.json', 'w', encoding='utf8')
laugh_key.write(json.dumps(laughter))
laugh_key.close()

# app = codecs.open('applause_count.json', 'w', encoding='utf8')
# app.write(json.dumps(applause))
# app.close()

app_key = codecs.open('applause_keywords.json', 'w', encoding='utf8')
app_key.write(json.dumps(applause))
app_key.close()
