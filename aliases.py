import json
from collections import defaultdict
aliases = defaultdict(lambda: {})

def main():
	aliases['1960']['John F. Kennedy'] = [u'Mr. KENNEDY', u'SENATOR KENNEDY', u'MR. KENNEDY']
	aliases['1960']['Richard Nixon'] = [u'MR. NIXON', u'Mr. NIXON']
	new_file = open('aliases.json', "w")
	new_file.write(json.dumps(aliases))
	new_file.close()

if __name__ == '__main__':
	main()