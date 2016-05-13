from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from scipy.misc import imread
import codecs, json
from collections import defaultdict
import string
import numpy as np
import seaborn

stop = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the","going","thats","know","think","dont","say","im","i","want","hes","like","didnt","ill","just","youre","id","ive","theres","theyre"]

wordcloud = WordCloud(max_font_size=100, relative_scaling=.5,background_color='white')

def plot_cloud(name,freq):
	shape = imread('america.jpg')
	wordcloud.mask = shape

	wordcloud_freq = wordcloud.generate_from_frequencies(freq)

	plt.figure()
	plt.imshow(wordcloud_freq)
	plt.axis("off")
	plt.savefig(name+'.png')
	plt.close()

def get_freq(name):
	newf = codecs.open(name+'_keywords.json','r',encoding='utf-8')
	f = json.load(newf)

	freq = defaultdict(int)

	for key,phrases in f.iteritems():
		for phrase in phrases:
			for sentence in phrase:
				for word in sentence:
					low_word = word.lower()
					fin_word = "".join(l for l in low_word if l not in string.punctuation)
					if fin_word not in stop:
						freq[fin_word] += 1

	plot_cloud(name,freq.items())

def plot_graph(name,val):
	y = np.arange(len(val))
	width = 0.25

	x = [v[1] for v in val]
	names = [v[0] for v in val]
	colors = [v[2] for v in val]

	plt.figure(figsize=(15,12))

	p1 = plt.barh(y,x,color=colors)
	p2 = plt.yticks(y+width,names,fontsize=12)
	plt.title('Top Candidates for Highest Average Counts of '+name.title(),fontsize=20)
	plt.xlabel('Average Count Per Debate',fontsize=16)
	plt.savefig(name+'_freq.png')
	plt.close()
	
def get_top(name):
	newf = codecs.open(name+'_count.json','r',encoding='utf-8')
	f = json.load(newf)

	lab = codecs.open('labels.json','r',encoding='utf-8')
	labels = json.load(lab)

	short_names = defaultdict(int)
	short_to_long = {}
	col_map = {'republican':'#841F27','democratic':'#354E71','independent':'#A5B557'}
	
	for key,val in f.iteritems():
		person = key.split(' ')
		year = person[-1]
		n = ' '.join(person[:-2])+' \''+year[-2:]
		short_names[n] += val
		short_to_long[n] = key

	top = sorted(filter(lambda x: short_names[x] > 0, short_names.keys()), key=short_names.get, reverse=True)

	plot_vals = []
	for person in top:
		plot_vals.append([person,short_names[person],col_map[labels[short_to_long[person]]]])
	
	plot_graph(name,plot_vals)

#get_freq('laughter')
#get_freq('applause')

print get_top('laughter')
print get_top('applause')