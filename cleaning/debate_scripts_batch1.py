import os
import re
import codecs
import json
from collections import defaultdict

#text = codecs.open('2012/republican/june_13_2011.txt','r',encoding='utf8').read()

def search(regex,fpath):
    """Find all matches of regex in the provided text"""
    regexp = re.compile(regex)
    results = list()
    text = codecs.open(fpath, 'r', encoding='utf8').read()
    for phrase in regexp.findall(text):
        results.append(phrase)
    return results

def get_dict(names, date, fpath):
	dictionary = {}
	for name in names:
		dictionary[name] = search(r''+name+':[\s\S]*?(?:[A-Z]:)',fpath)
	return dictionary

def all_debates(names):
	repub_debaters = defaultdict()
	for filename in os.listdir('../2012/republican'):
		filepath = '../2012/republican/'+filename
		f = codecs.open(filepath,'r',encoding='utf-8') 
		date = filename.replace('.txt','')
		date_dict = {}
		date_dict = get_dict(debaters, date, filepath)
		for k,v in date_dict.iteritems():
			repub_debaters[k] = repub_debaters.get(k,{})
			repub_debaters[k][date] = v
		f.close()
	return repub_debaters

debaters = ['BACHMANN', 'CAIN', 'GINGRICH', 'PAUL', 'PAWLENTY', 'ROMNEY', 'SANTORUM','HUNTSMAN','PERRY','JOHNSON']
republicans = {}
republicans = all_debates(debaters)

for k,v in republicans.iteritems():
	print k
#print republicans[k].keys()
print republicans['HUNTSMAN']

new_file = open('../data/2012_republicans', "w")
new_file.write(json.dumps(republicans))
new_file.close() 

# debaters = ['TRUMP','CRUZ','RUBIO','KASICH','CARSON','BUSH','GILMORE','CHRISTIE','FIORINA','SANTORUM','PAUL','HUCKABEE']
# republicans = {}
# republicans = all_debates(debaters)

# # print republicans.keys()
# # print republicans.values()
# new_file = open('data/2016_republicans', "w")
# new_file.write(json.dumps(republicans))
# new_file.close() 

# debaters = ['CLINTON','SANDERS','MALLEY','SUPREME']
# democrats = {}
# democrats = all_debates(debaters)
# print democrats.keys()
# print democrats.values()

# new_file = open('data/2016_democrats', "w")
# new_file.write(json.dumps(democrats))
# new_file.close()
