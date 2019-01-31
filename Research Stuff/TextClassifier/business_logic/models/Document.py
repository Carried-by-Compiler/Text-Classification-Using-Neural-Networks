import numpy as np
from gensim.models.doc2vec import TaggedDocument


class Document:

    def __init__(self, name: str, topic: str, path: str):
        self._name = name
        self._topic = topic
        self._path = path
        self._content = ""
        self._content_preprocessed = ""
        self._vector = None

    def get_name(self) -> str:
        return self._name

    def get_topic(self) -> str:
        return self._topic

    def get_path(self) -> str:
        return self._path

    def set_content(self, content: str):
        self._content = content

    def set_content_preprocessed(self, content: np.array):
        self._content_preprocessed = content

    def get_content(self) -> str:
        return self._content

    def set_vector(self, vector: np.array):
        self._vector = vector

    def get_vector(self) -> np.array:

        if self._vector is not None:
            return self._vector
        else:
            print("ERROR: %s" % ("Vector for " + self._name + " is not available"))

    def get_tagged_document(self):

        if self._content_preprocessed != "":
            return TaggedDocument(self._content_preprocessed, [self._name])
        else:
            print("document content not preprocessed!")
