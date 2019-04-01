# Class imports
from business_logic.models.word2vec import W2V
from business_logic.managers.observer_dp import Publisher
from business_logic.readers.reader_factory import ReaderFactory
from business_logic.data_retriever import DataRetriever

# Other imports
from tkinter import filedialog
from os import listdir


class W2VResultKeys:
    STATE = "STATE"
    FILES = "FILES"
    STATUS = "STATUS"
    WORDS = "WORDS"


class W2VManagerStates:
    W2V_FILES = 7
    SIMILAR_WORDS = 8
    TRAIN_W2V_STATUS = 9


class W2VManager(Publisher):

    def __init__(self, retriever: DataRetriever):
        self.__model = W2V()
        self.__observers = list()
        self.__state = dict()
        self.__retriever = retriever
        self.__file_reader = ReaderFactory.create_reader(ReaderFactory.TEXT, "W2V")

    def add_w2v_folder(self):
        filepath = filedialog.askdirectory(initialdir=".")

        if filepath == '':
            print("No file was selected")
        else:
            self.__model.refresh()
            files = listdir(filepath)
            if len(files) != 0:
                self.__state.clear()
                self.__state["STATE"] = W2VManagerStates.W2V_FILES
                self.__state["FILES"] = files
                self.__file_reader.add_path(filepath)
                self.notify_observers()
            else:
                print("W2VManager: No files in directory: " + filepath)

    def train_word2vec(self):
        lines = list(self.__file_reader.yield_line())
        ret = self.__model.train_model(lines)

        self.__state.clear()
        if ret == 1:
            self.__state["STATE"] = W2VManagerStates.TRAIN_W2V_STATUS
            self.__state["STATUS"] = "SUCCESS"
        else:
            self.__state["STATE"] = W2VManagerStates.TRAIN_W2V_STATUS
            self.__state["STATUS"] = "ERROR"
        self.notify_observers()

    def find_similar_words(self):
        input_word = self.__retriever.get_word()
        try:
            similarity = self.__model.get_similar_words(input_word)
        except KeyError as e:
            print(str(e))
            similarity = ""

        self.__state.clear()
        self.__state["STATE"] = W2VManagerStates.SIMILAR_WORDS
        self.__state["WORDS"] = similarity
        self.notify_observers()

    def attach(self, observer):
        self.__observers.append(observer)

    def notify_observers(self):
        for observer in self.__observers:
            observer.update(self.__state)
