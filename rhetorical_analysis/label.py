import json
import codecs

f = open('../clean_data_formats/full_parsed.json')
text = json.load(f)

candidates = {}

pres_map = {'Jimmy Carter presidential 1976':'democratic','Richard Nixon presidential 1960':'republican','Jimmy Carter presidential 1980':'democratic','Walter F. Mondale presidential 1984':'democratic','Mitt Romney presidential 2012':'republican',
'Bill Clinton presidential 1992':'democratic','Bill Clinton presidential 1996':'democratic','John Anderson presidential 1980':'republican','Ross Perot presidential 1992':'independent','Ronald Reagan presidential 1984':'republican','Ronald Reagan presidential 1980':'republican',
'Bob Dole presidential 1996':'republican','John McCain presidential 2008':'republican','George H. W. Bush presidential 1992':'republican','Al Gore presidential 2000':'democratic','John Kerry presidential 2004':'democratic','George H. W. Bush presidential 1988':'republican',
'Barack Obama presidential 2008':'democratic','Michael Dukakis presidential 1988':'democratic','George W. Bush presidential 2004':'republican','George W. Bush presidential 2000':'republican','Gerald Ford presidential 1976':'republican',
'John F. Kennedy presidential 1960':'democratic','Barack Obama presidential 2012':'democratic'}

for name in text.keys():
	if 'presidential' in name:
		candidates[name] = pres_map[name]
	else: 
		title = name.split(' ')
		candidates[name] = ''.join(title[len(title)-2:len(title)-1])

labels = codecs.open('labels.json' , 'w', encoding='utf-8')
labels.write(json.dumps(candidates))
labels.close()


