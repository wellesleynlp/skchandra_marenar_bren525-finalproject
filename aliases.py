import json
from collections import defaultdict
aliases = defaultdict(lambda: {})

def main():
	aliases['1960']['John F. Kennedy'] = [u'Mr. KENNEDY', u'SENATOR KENNEDY', u'MR. KENNEDY', u'John F. Kennedy']
	aliases['1960']['Richard Nixon'] = [u'MR. NIXON', u'Mr. NIXON', u'Richard Nixon']
	aliases['2012']['Barack Obama'] = [u'Barack Obama']
	aliases['2012']['Mitt Romney'] = [u'Mitt Romney']
	aliases['2012']['Michele Bachmann'] = [u'Michele Bachmann']
	aliases['2012']['Herman Cain'] = [u'Herman Cain']
	aliases['2012']['Newt Gingrich'] = [u'Newt Gingrich']
	aliases['2012']['Ron Paul'] = [u'Ron Paul']
	aliases['2012']['Tim Pawlenty'] = [u'Tim Pawlenty']
	aliases['2012']['Rick Santorum'] = [u'Rick Santorum']
	aliases['2012']['Jon Huntsman'] = [u'Jon Huntsman']
	aliases['2012']['Rick Perry'] = [u'Rick Perry']
	aliases['2012']['Gary Johnson'] = [u'Rick Johnson']
	aliases['2012']['Fred Karger'] = [u'Fred Karger']
	aliases['2012']['Buddy Roemer'] = [u'Buddy Roemer']
	aliases['2016']['Donald Trump'] = [u'Donald Trump']
	aliases['2016']['Ted Cruz'] = [u'Ted Cruz']
	aliases['2016']['Marco Rubio'] = [u'Marco Rubio']
	aliases['2016']['John Kasich'] = [u'John Kasich']
	aliases['2016']['Ben Carson'] = [u'Ben Carson']
	aliases['2016']['Jeb Bush'] = [u'Jeb Bush']
	aliases['2016']['Jim Gilmore'] = [u'Jim Gilmore']
	aliases['2016']['Chris Christie'] = [u'Chris Christie']
	aliases['2016']['Carly Fiorina'] = [u'Carly Fiorina']
	aliases['2016']['Rick Santorum'] = [u'Rick Santorum']
	aliases['2016']['Rand Paul'] = [u'Rand Paul']
	aliases['2016']['Mike Huckabee'] = [u'Mike Huckabee']
	aliases['2016']['Hillary Clinton'] = [u'Hillary Clinton']
	aliases['2016']['Bernie Sanders'] = [u'Bernie Sanders']
	aliases['2016']['Martin O\'Malley'] = [u'Martin O\'Malley']
	aliases['2016']['Vermin Supreme'] = [u'Vermin Supreme']
	new_file = open('aliases.json', "w")
	new_file.write(json.dumps(aliases))
	new_file.close()

if __name__ == '__main__':
	main()



