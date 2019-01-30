import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from DataSetBuilder import DataSetBuilder
from FileHandler import FileHandler
from TopicClassifier import TopicClassifier
import gensim
import numpy as np


def fill_data(name=""):
    db_builder = DataSetBuilder()
    db_builder.fill("Computer")


def make_file(name, folder):
    db_builder = DataSetBuilder()
    db_builder.make_file(name, folder)


if __name__ == "__main__":
    """
    make_file("William Shakespeare", "Literature")
    """
    docs = list()
    # Find a better way of getting the labels for training!
    labels = [[0, 0, 0, 1],
              [0, 1, 0, 0],
              [0, 0, 1, 0],  # 3
              [1, 0, 0, 0],
              [1, 0, 0, 0],
              [1, 0, 0, 0],
              [1, 0, 0, 0],
              [1, 0, 0, 0],
              [1, 0, 0, 0],
              [1, 0, 0, 0],
              [1, 0, 0, 0],  # 11
              [0, 1, 0, 0],
              [0, 0, 1, 0],
              [0, 1, 0, 0],
              [0, 1, 0, 0],
              [0, 1, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 0, 1],  # 18
              [0, 0, 1, 0],
              [0, 0, 1, 0],
              [0, 0, 1, 0],
              [0, 0, 1, 0],  # 22
              [0, 0, 1, 0],
              [0, 0, 0, 1],
              [1, 0, 0, 0],
              [0, 0, 0, 1],  # 26
              [0, 0, 1, 0],
              [0, 1, 0, 0],
              [0, 0, 0, 1],
              [0, 0, 0, 1],
              [0, 1, 0, 0],
              [0, 0, 0, 1],
              [0, 0, 0, 1],
              [1, 0, 0, 0],
              [0, 1, 0, 0],  # 35
              [0, 0, 0, 1],
              [0, 0, 1, 0],
              [0, 0, 0, 1],
              [0, 1, 0, 0]]  # 39

    file_handler = FileHandler()
    file_handler.update_path(folder="Test")
    model = gensim.models.Doc2Vec.load(file_handler.get_models_folder() + "\\exampleEPOCH600.d2v")
    for i in range(len(model.docvecs)):
        docs.append(model.docvecs[i])

    x = np.array(docs, ndmin=2)
    y = np.array(labels, ndmin=2)
    classifier = TopicClassifier()
    classifier.train(np.array(docs, ndmin=2), np.array(labels, ndmin=2))

    document = file_handler.read_preprocessed("Accounting.txt")
    new_document = np.array(model.infer_vector(document), ndmin=2)
    ret = classifier.predict(new_document)
    print(ret)
    """ 
    
    """

"""
    # Building the Doc2Vec model
    file_handler = FileHandler()
    file_handler.update_path("All")
    documents = list(file_handler.read_corpus())
    
    model = gensim.models.Doc2Vec(vector_size=3, min_count=2, epochs=600)
    model.build_vocab(documents)
    model.train(documents, total_examples=model.corpus_count, epochs=model.epochs)
    model.save(file_handler.get_models_folder() + "\\exampleEPOCH600.d2v")
"""


