from gensim.models.doc2vec import Doc2Vec
import logging
from os.path import join
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn import metrics
import os 
import gensim
from gensim.utils import simple_preprocess
from tkinter import filedialog
from tkinter import *
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class D2V:

    def __init__(self):
        
        self.__model = Doc2Vec(dm=1,
                               vector_size=300,
                               min_count=5,
                               epochs=50,
                               workers=8)

    
    def train(self, train_corpus):
        self.__model.build_vocab(train_corpus)
        self.__model.train(train_corpus, total_examples=self.__model.corpus_count, epochs=self.__model.epochs)
        return 1

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
        """
        Returns the labels of all documents within the Doc2Vec model
        """
        return list(self.__model.docvecs.doctags.keys())

    def get_doc_vec(self, identifier: str):
        return self.__model.docvecs[identifier]

class FileReader:

    def __init__(self):
        self.__models_paths = "D:\\workspace\\Text-Classification-Using-Neural-Networks\\src\\DocumentClassifier\\doc2vec_models"
        self.__training_path = "D:\\workspace\\FYP_dataset\\training"
        self.__testing_path = "D:\\workspace\\FYP_dataset\\testing"

    def read_corpus_train(self):

        print("READING CORPUS")
        topics = dirs = os.listdir(self.__training_path)
        
        # Go through each foler in dataset; where folder_name = topic of documents in that folder
        for topic in dirs:
            print("Current topic: {}".format(topic))
            curr_path = os.path.join(self.__training_path, topic)
            docs = os.listdir(curr_path)

            # Create TaggedDocument objects for each document in that folder
            for i, document in enumerate(docs):
                curr_doc_write = os.path.join(curr_path, document)
                with open(curr_doc_write, mode="r", encoding="utf-8") as file:
                    content = file.read()

                doc_id = topic + "__" + str(i) 
                yield gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(content), [doc_id])

    def get_models_path(self): return self.__models_paths
    def get_training_path(self): return self.__training_path
    def get_testing_path(self): return self.__testing_path

    def process_new_doc(self, filename):
        curr_doc_write = os.path.join(self.__testing_path, filename)
        with open(curr_doc_write, mode="r", encoding="utf-8") as file:
                    content = file.read()
        return gensim.utils.simple_preprocess(content)

class NN:

    def __init__(self):
        self.__topics = list()
        self.clf = MLPClassifier(activation='tanh', 
                                 learning_rate="adaptive", 
                                 learning_rate_init=0.001,
                                 solver="adam",
                                 max_iter=500)

    def train(self, x: np.array, y: np.array) -> None:
        result = self.clf.fit(x, y)
        print("Training error: {}".format(result.score(x, y)))

    def predict_probability(self, x: np.array) -> np.array:
        val = self.clf.predict_proba(x)
    
        return val

    def predict(self, x: np.array) -> np.array:
        val = self.clf.predict(x)
    
        return val
    
    def get_topics(self): return self.__topics

    def add_topic(self, t: str):
        if t not in self.__topics:
            self.__topics.append(t)

    def get_topic_vector(self, t: str):
        topic_vec = list()
        for topic in self.__topics:
            if t == topic:
                topic_vec.append(1)
            else:
                topic_vec.append(0)

        return topic_vec

reader = FileReader()
model = D2V()
classifier = NN()

model_name = "Sample_1.d2v"

# All contents of the lists below should be vectorized
train_topics = list()
train_docs = list() 

test_topics = list()
test_docs = list() 

def load_trainset():
    """
    Use this function when a trained Doc2Vec model exists. This function assumes
    that a Doc2Vec model is already loaded into the program. The NN classifier
    is used to store the necessary topics into the program.
    """
    doc_labels = model.get_labels()
    train_topics.clear()
    train_docs.clear()
    
    for label in doc_labels:
        train_docs.append(model.get_doc_vec(label))
        
        split_string = label.split("__")
        
        train_topics.append(split_string[0])
        classifier.add_topic(split_string[0])
    
    for i in range(len(train_topics)):
        train_topics[i] = classifier.get_topic_vector(train_topics[i])

def load_testset():
    
    test_topics.clear()
    test_docs.clear()
    
    print("Loading test dataset")
    topics = classifier.get_topics()
    
    for topic in topics:
        print("Current topic: %s" % topic)
        file_location = os.path.join(reader.get_testing_path(), topic)
        files = os.listdir(file_location)
        
        for file in files:
            with open(os.path.join(file_location, file), mode="r", encoding="utf-8") as file:
                    content = file.read()
            cleaned_doc = simple_preprocess(content)
            
            test_topics.append(topic)
            test_docs.append(model.infer_doc(cleaned_doc))
    
    for i in range(len(test_topics)):
        test_topics[i] = classifier.get_topic_vector(test_topics[i])
    
    print("Finished loading test set")

def train_d2v():
    train_corpus = list(reader.read_corpus_train())
    
    r = model.train(train_corpus)
    if r == 1:
        model.save(reader.get_models_path(), model_name)
        print("Doc2Vec training complete & saved!")

#train_d2v() 
model.load(reader.get_models_path(), model_name)
load_trainset()
load_testset()

classifier = NN()
print(train_docs)
classifier.train(np.array(train_docs, ndmin=2), np.array(train_topics, ndmin=2))
print("Training complete")

test_guesses = classifier.predict(np.array(test_docs, ndmin=2))
print(metrics.accuracy_score(np.array(test_topics, ndmin=2),test_guesses))