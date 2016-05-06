"""Build term-document matrix from collection of documents."""

import scipy
import scipy.sparse.linalg
from scipy.spatial.distance import cdist
import numpy
from collections import defaultdict
import json
import codecs
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer



def tfidf_docterm(corpus, freqthresh):
    """Estimate document-term TF-IDF vectors for each document (line in filename),
    where each column is a word, in decreasing order of frequency.
    Ignore words that appear fewer than freqthresh times.
    Return a list consisting of
    1. a list of the m word types with at least freqthresh count, sorted in decreasing order of frequency.
    2. an array with d rows and m columns,
    where row i is the vector for the ith document in filename,
    and col j represents the jth word in the above list.
    """
    common = stopwords.words('english')
    tfidf_dict = dict()
    candidate_dict = {}
    wordcounts = defaultdict(int)
    new_corpus = []
    labels = []
    for candidate in corpus.keys(): 
        if candidate == 'Hillary Clinton republican 2008':
            continue
        labels.append(candidate)
        debates = [debate for debates in corpus[candidate].values() for debate in debates]
        for word in debates:
                if word not in common:
                    wordcounts[word] +=1
        new_corpus.append([candidate, debates])
    
    sorted_words = sorted(filter(lambda x: wordcounts[x] >= freqthresh, wordcounts.keys()), key=lambda x: wordcounts[x], reverse=True)
    thresholded_words = set(sorted_words)
    word_indices = dict((word, index) for index, word in enumerate(sorted_words))
    context = numpy.zeros((len(new_corpus), len(sorted_words)))
    for di, doc in enumerate(new_corpus):
        for word in doc[1]:
            try:
                #print word
                if word in thresholded_words:
                    context[di,word_indices[word]] +=1
            except: 
                pass
    return [sorted_words, context, labels]

if __name__ == "__main__":
    f = codecs.open('full_parsed.json', 'r', encoding='utf-8')
    data = json.load(f)
    f.close()

    tfidf_vectors = tfidf_docterm(data,50)
    vectors = tfidf_vectors[1].tolist()
    names = tfidf_vectors[2]
    
    newf = codecs.open('tfidf_vectors.json' , 'w', encoding='utf-8')
    newf.write(json.dumps(dict(zip(names,vectors))))
    newf.close()