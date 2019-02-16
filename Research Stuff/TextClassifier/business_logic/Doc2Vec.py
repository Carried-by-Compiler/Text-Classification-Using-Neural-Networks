from gensim.models import Doc2Vec
from business_logic.DataStorer import DataStorer
import logging
import numpy as np
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class D2V:

    def __init__(self):
        self.__model = Doc2Vec(vector_size=4, min_count=1, epochs=100, workers=8)

    def train_model(self, data_store: DataStorer):
        self.__model.build_vocab(data_store)
        self.__model.train(data_store, total_examples=self.__model.corpus_count,
                           epochs=self.__model.epochs)

        return 1

    def get_docs_with_vectors(self):

        for i in range(len(self.__model.docvecs)):
            yield self.__model.docvecs[i]

    def get_doc_vec(self, identifier: str):
        return self.__model.docvecs[identifier]

    def get_model(self):
        return self.__model

    def infer_new_document(self, doc):
        new_document = np.array(self.__model.infer_vector(doc), ndmin=2)
        return new_document
