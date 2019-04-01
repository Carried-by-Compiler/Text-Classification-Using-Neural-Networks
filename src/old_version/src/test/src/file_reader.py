import os 
import gensim
from gensim.utils import simple_preprocess
from tkinter import filedialog
from tkinter import *

class FileReader:

    def __init__(self):
        self.__models_paths = filedialog.askdirectory(initialdir=".", title="Select Doc2Vec model folder")
        #self.__training_path = filedialog.askdirectory(initialdir=".", title="Select training folder")
        self.__testing_path = filedialog.askdirectory(initialdir=".", title="Select testing folder")

    def read_corpus_train(self):

        print("READING CORPUS")
        topics = dirs = os.listdir(self.__training_path)
        
        for topic in dirs:
            print("Current topic: {}".format(topic))
            curr_path = os.path.join(self.__training_path, topic)
            docs = os.listdir(curr_path)

            for i, document in enumerate(docs):
                curr_doc_write = os.path.join(curr_path, document)
                with open(curr_doc_write, mode="r", encoding="utf-8") as file:
                    content = file.read()

                doc_id = topic + "__" + str(i) 
                yield gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(content), [doc_id])

    def get_models_path(self): return self.__models_paths

    def process_new_doc(self, filename):
        curr_doc_write = os.path.join(self.__testing_path, filename)
        with open(curr_doc_write, mode="r", encoding="utf-8") as file:
                    content = file.read()
        return gensim.utils.simple_preprocess(content)
