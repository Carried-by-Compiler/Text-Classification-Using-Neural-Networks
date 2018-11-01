import gzip
from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
import logging
from wikipedia import page, search
from StemmingHelper import StemmingHelper as hs
import numpy as np
"""
def read_input(input_file):
    This method reads the input file which is in gzip format

    logging.info("reading file {0}...this may take a while".format(input_file))

    with gzip.open(input_file, 'rb') as f:
        for i, line in enumerate(f):

            print(line)
            break
"""


if __name__ == "__main__":

    #documents = list(read_input("./sentences.zip"))
    titles = search("Computer")
    wikipage = page(titles[0])

    f = open("../TextFiles/wikipage.txt", "r")

    sentence = ""

    for line in f:
        sentence += line

    # TODO: Create a file accessor to create sentences from a file
    # TODO: Research iterators and generators to help output sentences
    splitSentence = sentence.split(".")
    print(splitSentence[0] + "\n" + splitSentence[1])

    f.close()


