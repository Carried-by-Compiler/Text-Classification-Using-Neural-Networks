import numpy as np
from os import path
from gensim.models.doc2vec import TaggedDocument


class Document:

    def __init__(self, name: str, topic: str, path: str):
        self.__id = ""
        self.__name = name
        self.__topic = topic
        self.__path = path
        self.__content = ""
        self.__content_preprocessed = ""
        self.__vector = None

    def get_id(self) -> str:
        return self.__id

    def set_id(self, counter: int):
        self.__id = self.__topic + "__" + str(counter)

    def get_name(self) -> str:
        return self.__name

    def get_topic(self) -> str:
        return self.__topic

    def get_path(self) -> str:
        return self.__path

    def get_full_path(self) -> str:
        return path.join(self.__path, self.__name)

    def set_content(self, content: str):
        self.__content = content

    def set_content_preprocessed(self, content: np.array):
        self.__content_preprocessed = content

    def get_content_preprocessed(self) -> np.array:
        return self.__content_preprocessed

    def get_content(self) -> str:
        return self.__content

    def set_vector(self, vector: np.array):
        self.__vector = vector

    def get_vector(self) -> np.array:

        if self.__vector is not None:
            return self.__vector
        else:
            print("ERROR: %s" % ("Vector for " + self.__name + " is not available"))