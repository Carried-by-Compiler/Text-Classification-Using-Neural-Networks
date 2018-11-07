import os
from SentenceProcessing import SentenceProcessor


class FileHandler:

    def __init__(self, text_file="TextFiles", saved_models="SavedModels"):
        """
        A class to handle file and text manipulation for the Word2Vec project. If passed in folder names
        do not exist, the folders are automatically made

        :param text_file: name of folder to store dataset
        :param saved_models: name of folder to store saved word2vec models
        """

        self.__path = os.path.dirname(os.path.abspath("."))
        self.text_file_path = os.path.join(self.__path, text_file)
        print(self.text_file_path)
        self.model_file_path = os.path.join(self.__path, saved_models)
        self.sentence_processor = SentenceProcessor(self.text_file_path)

        if not os.path.exists(self.text_file_path):
            os.mkdir(self.text_file_path)

        if not os.path.exists(self.model_file_path):
            os.mkdir(self.model_file_path)

    def print_to_file(self, file_name: str, content: str):
        """
        Prints to file
        :param file_name: name of file to be created
        :param content: string to be printed to the file
        """

        f = open(self.text_file_path + "\\" + file_name + ".txt", mode="w", encoding="utf-8")
        f.write(content)
        f.close()

    def get_file_contents(self, filename: str):

        with open(os.path.join(self.text_file_path, filename), "r", encoding="utf-8") as f:
            read_data = f.read()

        return read_data

    def get_sentence_processor_iterator(self):

        return self.sentence_processor