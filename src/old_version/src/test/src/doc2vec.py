from gensim.models.doc2vec import Doc2Vec
import logging
from os.path import join
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class D2V:

    def __init__(self):
        
        self.__model = Doc2Vec(dm=1,
                               vector_size=300,
                               min_count=5,
                               epochs=15,
                               workers=8)

    
    def train(self, train_corpus):
        self.__model.build_vocab(train_corpus)
        self.__model.train(train_corpus, total_examples=self.__model.corpus_count, epochs=self.__model.epochs)

    def save(self, folder_path, filename):
        self.__model.save(join(folder_path, filename))

    def load(self, folder_path, filename):
        self.__model = Doc2Vec.load(join(folder_path, filename))

    def infer_doc(self, doc):
        return self.__model.infer_vector(doc)

    def get_vector(self, id):
        return self.__model.docvecs[id]

    def get_similar(self, doc):
        return self.__model.docvecs.most_similar([doc])

    def get_labels(self):
        return list(self.__model.docvecs.doctags.keys())

    def get_doc_vec(self, identifier: str):
        return self.__model.docvecs[identifier]
