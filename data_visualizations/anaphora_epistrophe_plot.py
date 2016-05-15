import matplotlib.pyplot as plt
import codecs, json
import numpy as np

N = 10
newf = codecs.open('../rhetorical_analysis/anaphora_epistrophe.json', 'r', encoding='utf-8')
f = json.load(newf)
labels = []
xdata = []
ydata = []
xmin = 1
ymin = 1
for key, l in f.iteritems():
	labels.append(key)
	xdata.append(l[0])
	ydata.append(l[1])
	if l[0] != 0 and l[0] < xmin:
		xmin = l[0]
	if l[1] != 0 and l[1] < ymin:
		ymin = l[1]
print labels[xdata.index(max(xdata))]
print labels[ydata.index(max(ydata))]
print xmin, max(xdata), ymin, max(ydata)

plt.subplots_adjust(bottom = 0.1)
plt.scatter(xdata, ydata, marker = 'o')
# for label, x, y in zip(labels, xdata, ydata):
#     plt.annotate(
#         label, 
#         xy = (x, y), xytext = (0, 5),
#         textcoords = 'offset points', ha = 'right', va = 'bottom',
#         bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5))
plt.title('Anaphora and Epistrophe Usage Distribution',fontsize=20)
plt.xlabel('Anaphora Normalized Count',fontsize=16)
plt.ylabel('Epistrophe Normalized Count', fontsize=16)
plt.savefig('unlabelled_ae_plot.png')
plt.close()
