from gensim.models import Doc2Vec
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class D2V:

    def __init__(self):
        self.__model = Doc2Vec(vector_size=3, min_count=2, epochs=500)
        print("Hi")

    def train_model(self, documents):
        self.__model.build_vocab(documents)
        self.__model.train(documents, total_examples=self.__model.corpus_count, epochs=self.__model.epochs)

        texts = ["Spam (food).txt", "Computer graphics (computer science).txt", "Computer graphics.txt"]
        for text in texts:
            print("%s: %s" % (text, self.__model[text]))
        return 1

    def get_model(self):
        return self.__model
