from __future__ import division
import sys
import numpy
from collections import defaultdict
import json
from nltk.corpus import stopwords
import codecs
import json

stops = stopwords.words('english')
stops.append('bell')
stops.append('rings')

"""This code was written by Sravana Reddy and adapted by our team in order to parse our data structure properly."""

"""Associate text features with each label, compute probabilities and MI"""

def feature_label_pmi(filename, labelname, feat_thresh):
    """Compute pointwise mutual information between features and user labels"""
    labels = defaultdict(set)  # {label: speakers of label}
    features = defaultdict(set)   # {feat: speakers who use feat}
    labels_features = defaultdict(set) # {feat, label: speakers of label who use feat}

    # count each user once
    # users = set()
    # for line in open(filename):
    #     userid, label, toktweet = line.split(',', 2)
    #     users.add(userid)
    #     labels[label].add(userid)
    #     for feature in set(toktweet.split()):  # word types in this case. can be any feature.
    #         features[feature].add(userid)
    #         labels_features[(feature, label)].add(userid)

    candidates = set()
    speeches = open(filename)
    text = json.load(speeches)
    label_cand = open(labelname)
    labels_dic = json.load(label_cand)

    for candidate,speech in text.iteritems():
        split_name = candidate.split(' ')
        name = ' '.join(split_name[:-2])
        candidates.add(name)
        label = labels_dic[candidate]
        labels[label].add(name)
        for day,feat in speech.iteritems():
            for feature in feat:
                if feature not in stops:
                    features[feature].add(name)
                    labels_features[(feature,label)].add(name)

    old_feat = {}
    #compute PMI
    pmi = defaultdict(lambda : defaultdict(float))
    numusers = len(candidates)
    for feature in features:
        old_feat[feature] = features[feature]
        features[feature] = len(features[feature])

    old_labels = {}

    for label in labels:
        old_labels[label] = labels[label]
        labels[label] = len(labels[label])
        for feature in features:
            if features[feature]>=feat_thresh:  # ignore infrequent features
                pmi[label][feature] = numpy.log2(len(labels_features[(feature, label)])*numusers/(features[feature]*labels[label]))

    rep = []
    dem = []
    rep_person_count = defaultdict(int)
    dem_person_count = defaultdict(int)

    for label in labels:
        if label == 'independent':
            continue
        print 'POSITIVE for', label
        for feature, score in sorted(filter(lambda x:x[1]>0, pmi[label].items()), key=lambda x:x[1], reverse=True):
            if label == 'republican':
                rep.append((feature,score))
                for name in old_feat[feature]:
                    if name in old_labels[label]:
                        rep_person_count[name] += 1
            elif label == 'democratic':
                dem.append((feature,score))
                for name in old_feat[feature]:
                    if name in old_labels[label]:
                        dem_person_count[name] += 1
            else:
                pass
            print feature,
        print

    print '\n','\n'
    print sorted(rep_person_count, key=rep_person_count.get, reverse=True),'\n','\n'
    print sorted(dem_person_count, key=dem_person_count.get, reverse=True)

    #print rep,'\n','\n',dem

    rep_file = codecs.open('rep_freq.json','w',encoding='utf-8')
    rep_file.write(json.dumps(rep))
    rep_file.close()
    
    dem_file = codecs.open('dem_freq.json','w',encoding='utf-8')
    dem_file.write(json.dumps(dem))
    dem_file.close()

if __name__=='__main__':
    filename = sys.argv[1]  #../clean_data_formats/full_parsed.json
    labelfile = sys.argv[2] #labels.json
    threshold = int(sys.argv[3])    #15
    feature_label_pmi(filename,labelfile,threshold)