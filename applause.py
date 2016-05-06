import os
import codecs
import json
import re
import indicoio
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

laughter = {}
applause = {}

for candidate,dates in f.iteritems():
	for date,speech in dates.iteritems():
		r1 = search(r'([\w|\'|\-|\, ]*\.){1,3} ?(?=\[Applause\])',speech)
		r2 = search(r'([\w|\'|\-|\, ]*\.){1,3} ?(?=\[applause\])',speech)
		r3 = search(r'([\w|\'|\-|\, ]*\.){1,3} ?(?=\(Applause\))',speech)
		r4 = search(r'([\w|\'|\-|\, ]*\.){1,3} ?(?=\(applause\))',speech)

		r5 = search(r'([\w|\'|\-|\, ]*\.){1,3} ?(?=\[Laughter\])',speech)
		r6 = search(r'([\w|\'|\-|\, ]*\.){1,3} ?(?=\[laughter\])',speech)
		r7 = search(r'([\w|\'|\-|\, ]*\.){1,3} ?(?=\(Laughter\))',speech)
		r8 = search(r'([\w|\'|\-|\, ]*\.){1,3} ?(?=\(laughter\))',speech)
		
		applause[candidate] = applause.get(candidate,0)+len(r1)+len(r2)+len(r3)+len(r4)
		laughter[candidate] = laughter.get(candidate,0)+len(r5)+len(r6)+len(r7)+len(r8)
	applause[candidate] = applause[candidate]/float(len(dates))
	laughter[candidate] = laughter[candidate]/float(len(dates))

laughter_keywords = {}
applause_keywords = {}

# for candidate,speech in laughter.iteritems():
# 	if speech:
# 		laughter_keywords[candidate] = sorted(indicoio.keywords(speech, version=2))

# for candidate,speech in applause.iteritems():
# 	if speech:
# 		applause_keywords[candidate] = sorted(indicoio.keywords(speech, version=2))

laugh = codecs.open('laughter_count.json' , 'w', encoding='utf-8')
laugh.write(json.dumps(laughter))
laugh.close()

# # laugh_key = codecs.open('laughter_keywords.json', 'w', encoding='utf8')
# # laugh_key.write(json.dumps(laughter_keywords))
# # laugh_key.close()

app = codecs.open('applause_count.json', 'w', encoding='utf8')
app.write(json.dumps(applause))
app.close()

# app_key = codecs.open('applause_keywords.json', 'w', encoding='utf8')
# app_key.write(json.dumps(applause_keywords))
# app_key.close()
