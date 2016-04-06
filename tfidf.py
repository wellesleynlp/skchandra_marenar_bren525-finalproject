"""Build term-document matrix from collection of documents."""

import scipy
import scipy.sparse.linalg
import numpy

__author__='Your name here'

def tfidf_docterm(filename, freqthresh):
    """Estimate document-term TF-IDF vectors for each document (line in filename),
    where each column is a word, in decreasing order of frequency.
    Ignore words that appear fewer than freqthresh times.
    Return a list consisting of
    1. a list of the m word types with at least freqthresh count, sorted in decreasing order of frequency.
    2. an array with d rows and m columns,
    where row i is the vector for the ith document in filename,
    and col j represents the jth word in the above list.
    """
    text, wordcounts = parsetextfile(filename) # read text and get word frequencies
    sorted_words = sorted(filter(lambda x: wordcounts[x] >= freqthresh, wordcounts.keys()), key = lambda x: wordcounts[x], reverse = True)
    thresholded_words = set(sorted_words)
    word_indices = dict((word, index) for index, word in enumerate(sorted_words))
    context = numpy.zeros((len(text), len(sorted_words)))
    for di, doc in enumerate(text):
        for word in doc:
            if word in thresholded_words:
                context[di,word_indices[word]] += 1
    return [sorted_words, context]

def dimensionality_reduce(vectors, ndims):
    """Apply SVD on original sparse matrix, return reduced vectors."""
    # Do not modify
    U, s, Vh = scipy.sparse.linalg.svds(vectors, k=ndims)
    sigmatrix = scipy.matrix(scipy.diag(s))
    return U * sigmatrix
