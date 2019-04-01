from gensim.models import Word2Vec
import multiprocessing
import logging

logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M:%S', level=logging.INFO)


class W2V:

    def __init__(self):
        cores = multiprocessing.cpu_count()
        self.__model = Word2Vec(iter=5, min_count=10, size=300, workers=cores - 1, window=10)

    def train_model(self, sentences):
        try:
            self.__model.build_vocab(sentences)
            self.__model.train(sentences, total_examples=self.__model.corpus_count,
                               epochs=self.__model.epochs)
            return 1
        except Exception as e:
            print(str(e))
            return -1

    def get_similar_words(self, word: str):
        return self.__model.wv.most_similar(positive=word)

    def refresh(self):
        del self.__model
        self.__init__()