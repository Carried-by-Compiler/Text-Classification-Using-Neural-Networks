from business_logic.models.doc2vec import D2V
from .observer_dp import Publisher
from business_logic.classifiers.classifier_factory import ClassifierFactory
from business_logic.readers.reader_factory import ReaderFactory
from business_logic.data_storer import DataStorer
from business_logic.data_retriever import DataRetriever
from tkinter import filedialog
from os import listdir
import numpy as np


class D2VResultKeys:
    STATE = "STATE"
    TOPIC = "TOPIC"
    TOPICS = "TOPICS"
    FILE = "FILE"
    FILES = "FILES"
    FILE_PATH = "FILE_PATH"
    STATUS = "STATUS"
    RESULTS = "RESULTS"


class D2VManagerStates:
    ADD_DIR = 1
    ADD_DATASET = 2
    LOAD_MODEL = 3
    TRAIN_D2V_STATUS = 4
    TRAIN_CLASSIFIER = 5
    CLASSIFIER_RESULT = 6


class D2VManager(Publisher):

    def __init__(self, data_retriever: DataRetriever):
        self.__observers = list()
        self.__model = D2V()
        self.__file_reader = ReaderFactory.create_reader(ReaderFactory.TEXT, "D2V")
        self.__classifier = ClassifierFactory.create_classifier(ClassifierFactory.NEURAL_NET)
        self.__data_handler = DataStorer()
        self.__info_retriever = data_retriever

        self.__state = dict()

    def add_directory(self):
        filepath = filedialog.askdirectory(initialdir=".")

        if filepath == '':
            print("No file was selected")
        else:
            split_path = filepath.split("/")
            topic = split_path[len(split_path) - 1]
            self.__data_handler.add_topic(topic)
            files = self.__file_reader.add_path(filepath)
            print("D2VManager: stored topics: " + str(self.__data_handler.get_topics()))

            self.__state.clear()
            self.__state[D2VResultKeys.STATE] = D2VManagerStates.ADD_DIR
            self.__state[D2VResultKeys.TOPIC] = topic
            self.__state[D2VResultKeys.FILE_PATH] = filepath
            self.__state[D2VResultKeys.FILES] = files

            self.notify_observers()

    def add_dataset(self):
        self.__state[D2VResultKeys.STATE] = D2VManagerStates.ADD_DATASET
        self.notify_observers()

        self.__data_handler.clear()
        self.__file_reader.clear_paths()

        dataset_path = filedialog.askdirectory(initialdir=".")
        if dataset_path == '':
            topics = None
        else:
            topics = listdir(dataset_path)

        if topics is None:
            print("d2v_manager: No folders in dataset")
        else:
            for topic in topics:
                self.__data_handler.add_topic(topic)
                full_path = dataset_path + "/" + topic
                files = self.__file_reader.add_path(full_path)
                print("D2VManager: stored topics: " + str(self.__data_handler.get_topics()))

                self.__state.clear()
                self.__state[D2VResultKeys.STATE] = D2VManagerStates.ADD_DIR
                self.__state[D2VResultKeys.TOPIC] = topic
                self.__state[D2VResultKeys.FILE_PATH] = full_path
                self.__state[D2VResultKeys.FILES] = files

                self.notify_observers()

    def load_model(self):
        model_path = filedialog.askopenfilename(initialdir="../doc2vec_models", title="Select Doc2Vec model",
                                                filetypes=(("Doc2Vec Models", "*.d2v"), ("All Files", "*")))

        if model_path == '':
            print("d2v_manager: No saved model selected")
        else:
            self.__data_handler.clear()
            self.__model.load_model(model_path)
            self.__load_data()
            topics = self.__data_handler.get_topics()

            self.__state.clear()
            self.__state[D2VResultKeys.STATE] = D2VManagerStates.LOAD_MODEL
            self.__state[D2VResultKeys.TOPICS] = topics

            self.notify_observers()

    def __load_data(self):
        labels = self.__model.get_labels()
        for label in labels:
            self.__data_handler.add_document(self.__model.get_doc_vec(label))
            split_string = label.split("__")
            # self.__data_handler.add_loaded_topic(split_string[0])
            self.__data_handler.add_topic(split_string[0])

    def train_doc2vec(self):
        print("D2VManager: Started Doc2Vec training")
        ret = self.__model.train_model(list(self.__file_reader.yield_documents()))

        self.__state.clear()
        if ret == 1:
            self.__state[D2VResultKeys.STATE] = D2VManagerStates.TRAIN_D2V_STATUS
            self.__state[D2VResultKeys.STATUS] = "SUCCESS"
        else:
            self.__state[D2VResultKeys.STATE] = D2VManagerStates.TRAIN_D2V_STATUS
            self.__state[D2VResultKeys.STATUS] = "ERROR"
        self.notify_observers()

    def train_classifier(self):
        docs = list()
        topics = list()

        print("D2VManager: Started classifier training")
        labels = self.__model.get_labels()
        for label in labels:
            split_label = label.split("__")

            curr_topic = split_label[0]
            curr_docvec = self.__model.get_doc_vec(label)

            docs.append(curr_docvec)
            topics.append(self.__data_handler.get_topic_vector(curr_topic))

        self.__classifier.train(np.array(docs, ndmin=2), np.array(topics, ndmin=2))

        self.__state.clear()
        self.__state[D2VResultKeys.STATE] = D2VManagerStates.TRAIN_CLASSIFIER
        self.notify_observers()
        print("Classifier trained!")

    def classify_document(self):
        content = self.__info_retriever.get_text()
        processed_content = self.__file_reader.process_text(content)
        new_docvec = self.__model.infer_new_document(processed_content)

        results = self.__classifier.predict(new_docvec)

        self.__state.clear()
        self.__state[D2VResultKeys.STATE] = D2VManagerStates.CLASSIFIER_RESULT
        self.__state[D2VResultKeys.TOPICS] = self.__data_handler.get_topics()
        self.__state[D2VResultKeys.RESULTS] = results

        self.notify_observers()

    def attach(self, observer):
        self.__observers.append(observer)

    def notify_observers(self):
        for observer in self.__observers:
            observer.update(self.__state)

