#!/usr/bin/env python2

from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import codecs, json
from scipy.misc import imread

wordcloud = WordCloud(max_font_size=100, relative_scaling=.5,background_color='white')

def plot(party,n):
	for num,name in enumerate(party):
		filename = codecs.open(name+'_freq.json','r',encoding='utf-8')
		text = json.load(filename)
		if name == 'rep':
			coloring = imread(name+'_logo.jpg')
		elif name == 'dem':
			coloring = imread(name+'_logo.png')

		wordcloud.mask = coloring
		wordcloud_party = wordcloud.generate_from_frequencies(text)
		image_colors = ImageColorGenerator(coloring)
		plt.figure()
		#plt.subplot(2,1,num+1)
		plt.imshow(wordcloud_party.recolor(color_func=image_colors))
		plt.axis("off")
		plt.savefig(name+str(n)+'.png')
		plt.close()

	#plt.show()

plot(['dem','rep'],1)

# for i in range(20):
# 	plot(['dem','rep'],i)
#plot('rep',2)
#plt.show()
