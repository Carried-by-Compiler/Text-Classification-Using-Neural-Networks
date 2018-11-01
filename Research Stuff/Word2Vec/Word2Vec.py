"""
Source code from: https://rare-technologies.com/word2vec-tutorial/

original author : Radim Řehůřek
"""
import gzip
from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import logging


def read_input(input_file):
    """This method reads the input file which is in gzip format"""

    logging.info("reading file {0}...this may take a while".format(input_file))

    with gzip.open(input_file, 'rb') as f:
        for i, line in enumerate(f):

            print(line)
            break

if __name__ == "__main__":

    documents = list(read_input("./sentences.zip"))

