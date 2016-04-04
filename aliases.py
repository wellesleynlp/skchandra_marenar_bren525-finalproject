import json
aliases = {}

def main():
	aliases['John F. Kennedy'] = [u'Mr. KENNEDY', u'SENATOR KENNEDY', u'MR. KENNEDY']
	aliases['Richard Nixon'] = [u'MR. NIXON', u'Mr. NIXON']
	new_file = open('data/aliases.json', "w")
	new_file.write(json.dumps(aliases))
	new_file.close()

if __name__ == '__main__':
	main()