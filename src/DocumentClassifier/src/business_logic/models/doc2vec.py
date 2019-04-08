from gensim.models import Doc2Vec
import logging
import multiprocessing
import numpy as np

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class D2V:

    def __init__(self):
        cores = multiprocessing.cpu_count()
        self.__model = Doc2Vec(vector_size=300, min_count=2, epochs=70, workers=cores - 1)

    def train_model(self, documents):
        try:
            self.__model.build_vocab(documents)
            self.__model.train(documents, total_examples=self.__model.corpus_count,
                               epochs=self.__model.epochs)
            return 1
        except Exception as e:
            print(str(e))
            return -1

    def infer_new_document(self, doc):
        new_document = np.array(self.__model.infer_vector(doc), ndmin=2)
        return new_document

    def get_doc_vec(self, identifier: str):
        return self.__model.docvecs[identifier]

    def get_labels(self):
        return list(self.__model.docvecs.doctags.keys())

    def save_model(self, save_path):
        self.__model.save(save_path)

    def load_model(self, load_path):
        self.__model = Doc2Vec.load(load_path)
        print("Loaded model:\n-------------")
        print("Vector size:\t" + str(self.__model.vector_size))
        print("Epochs:\t" + str(self.__model.epochs))

    def refresh(self):
        del self.__model
        self.__init__()