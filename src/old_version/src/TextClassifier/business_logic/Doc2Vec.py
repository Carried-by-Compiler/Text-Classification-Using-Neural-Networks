from gensim.models import Doc2Vec
from business_logic.DataStorer import DataStorer
import logging
import numpy as np
import os
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class D2V:

    def __init__(self):
        self.__model = Doc2Vec(vector_size=300, min_count=2, epochs=100, workers=8)

    def train_model(self, data_store: DataStorer):
        self.__model.build_vocab(data_store)
        self.__model.train(data_store, total_examples=self.__model.corpus_count,
                           epochs=self.__model.epochs)

        return 1

    def save_model(self, path: str):
        self.__model.save(path)

    def load_model(self, path: str):
        self.__model = Doc2Vec.load(path)

    def get_labels(self):
        return list(self.__model.docvecs.doctags.keys())

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

    def infer(self, doc):
        return self.__model.infer_vector(doc)

    def get_similar(self, doc: np.array):
        print(self.__model.docvecs.most_similar(positive=[doc], topn=10))

    def refresh(self):
        del self.__model
        self.__init__()
