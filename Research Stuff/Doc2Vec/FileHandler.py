from os import path, listdir
import gensim.models.doc2vec as doc2vec
from gensim.utils import simple_preprocess

class FileHandler:
    """
    This class will be used to perform file manipulation for this program
    """

    def __init__(self):
        self.__path = path.dirname(path.abspath(__file__))
        self.__models = path.join(self.__path, "Models")


    def update_path(self, folder=""):
        """
        Update the file path to the source where read and write operations should take place.
        :param folder: the name of the folder
        """
        self.__path = path.join(self.__path, folder)

    def write(self, content, filename):
        """
        Write to to current file path.
        :param content: What the file should contain
        :param filename: What the file should be called
        """
        print("Currently printing file: %s" % filename)
        f = open(self.__path + "\\" + filename + ".txt", mode="w", encoding="utf-8")
        f.write(content)
        f.close()

    def read(self, filename):
        """
        Read from a file
        :param filename: The name of the file
        :return: The contents of the file
        """
        f = path.join(self.__path, filename + ".txt")
        with open(f, mode="r", encoding="utf-8") as file:
            content = file.read()

        return content

    def read_preprocessed(self, filename):
        """
        Read from a file. This function returns the content of the file as
        pre-processed.
        :param filename: The name of the file to read from
        :return: The pre-processed version of the file.
        """
        f = path.join(self.__path, filename)
        with open(f, mode="r", encoding="utf-8") as file:
            content = file.read()

        return simple_preprocess(content)

    def read_corpus(self):
        """
        Get all documents in the current folder in TaggedDocuments type
        :return: generator of documents to product TaggedDocuments
        """
        files = listdir(self.__path)
        for i, document in enumerate(files):
            content = self.read_preprocessed(document)
            yield doc2vec.TaggedDocument(content, [document])

    def read_as_tagged_document(self, filename):
        """
        Read in a single document as a TaggedDocument object
        :param filename: The name of the file
        :return: A TaggedDocument object
        """
        f = path.join(self.__path, filename)
        content = self.read_preprocessed(filename)
        return doc2vec.TaggedDocument(content, [filename])

    def get_models_folder(self):
        return self.__models
