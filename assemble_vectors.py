import codecs
import json
from collections import defaultdict

aejson = codecs.open('anaphora_epistrophe.json' , 'r', encoding='utf-8')
ajson = codecs.open('applause_count.json' , 'r', encoding='utf-8')
ljson = codecs.open('laughter_count.json' , 'r', encoding='utf-8')
tfjson = codecs.open('tfidf_vectors.json' , 'r', encoding='utf-8')
ae = json.load(aejson)
a = json.load(ajson)
l = json.load(ljson)
tf = json.load(tfjson)

def assemble_vectors():
	resultsdict = defaultdict(lambda: [])
	for candidate, applause in a.iteritems():
		laughter = l[candidate]
		anaphora = ae[candidate][0]
		epistrophe = ae[candidate][1]
		tfidf = tf[candidate]
		resultsdict[candidate] += tfidf
		resultsdict[candidate].append(applause)
		resultsdict[candidate].append(laughter)
		resultsdict[candidate].append(anaphora)
		resultsdict[candidate].append(epistrophe)
	newf = codecs.open('assembled_vectors.json' , 'w', encoding='utf-8')
	newf.write(json.dumps(resultsdict))
	newf.close()

if  __name__ == '__main__':
	assemble_vectors()