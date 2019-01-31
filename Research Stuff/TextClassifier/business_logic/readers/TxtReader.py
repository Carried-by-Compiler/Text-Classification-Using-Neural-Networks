from business_logic.readers.IReader import IReader
from business_logic.textprocessors.GensimTextProcessor import GensimTextProcessor
from business_logic.models.Document import Document
from gensim.models.doc2vec import TaggedDocument
import numpy as np
from os import listdir, path


class TxtReader(IReader):
    """
    This class is used to read documents of txt file format. It also
    stores the topics associated with each file path
    """

    def __init__(self):
        self.__paths = dict()
        self.__files = dict()
        self.__documents = list()

        # try to use factory method here
        self.__text_processor = GensimTextProcessor()

    def add_path(self, directory: str, topic: str) -> list:

        files = []

        if directory not in self.__paths:

            self.__paths[directory] = topic
            files = listdir(directory)

            for file in files:
                if directory in self.__files:
                    self.__files[directory].append(file)
                else:
                    self.__files[directory] = [file]

        else:
            print("Key already exists")

        return files

    def remove_path(self, directory: str):
        del self.__paths[directory]

    def print_paths(self):
        for d in self.__paths:
            print(d, "=>", self.__paths[d])

    def clear_paths(self):
        self.__paths.clear()

    def load_documents(self):
        """
        Load the documents into the program
        """

        if len(self.__files) == 0:
            yield False
        else:
            for directory, files in self.__files.items():

                for file in files:

                    full_path = path.join(directory, file)
                    with open(full_path, mode="r", encoding="utf-8") as f:
                        content = f.read()

                    processed_text = self.__process_text(content)

                    new_document = Document(name=file, topic=self.__paths[directory], path=directory)
                    new_document.set_content(content)
                    new_document.set_content_preprocessed(processed_text)
                    self.__documents.append(new_document)

                    yield TaggedDocument(processed_text, [file])


        """
        if len(self.__paths) != 0:

            for directory, topic in self.__paths.items():
                files = listdir(directory)

                for file in files:
                    file_path = path.join(directory, file)
                    with open(file_path, mode="r", encoding="utf-8") as f:
                        content = f.read()

                    processed_text = self.__process_text(content)

                    new_document = Document(name=file, topic=topic, path=directory)
                    new_document.set_content(content)
                    new_document.set_content_preprocessed(processed_text)

                    self.__documents.append(new_document)

            return True
        else:
            return False
        """

    def __process_text(self, txt: str) -> list:

        processed_text = self.__text_processor.process_text(text=txt)
        return processed_text
