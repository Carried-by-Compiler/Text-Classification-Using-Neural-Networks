from business_logic.readers.IReader import IReader
from business_logic.textprocessors.GensimTextProcessor import GensimTextProcessor
from business_logic.models.Document import Document
import numpy as np
from os import listdir, path


class TxtReader(IReader):
    """
    This class is used to read documents of txt file format. It also
    stores the topics associated with each file path
    """

    def __init__(self):
        self.paths = {}
        self.documents = []

        # try to use factory method here
        self._text_processor = GensimTextProcessor()

    def add_path(self, directory: str, topic: str) -> list:

        files = []

        if directory not in self.paths:
            self.paths[directory] = topic
            files = listdir(directory)
        else:
            print("Key already exists")

        return files

    def remove_path(self, directory: str):
        del self.paths[directory]

    def print_paths(self):
        for d in self.paths:
            print(d, "=>", self.paths[d])

    def clear_paths(self):
        self.paths.clear()

    def load_documents(self) -> bool:
        """
        Load the documents into the program
        """

        if len(self.paths) != 0:

            for directory, topic in self.paths.items():
                files = listdir(directory)

                for file in files:
                    file_path = path.join(directory, file)
                    with open(file_path, mode="r", encoding="utf-8") as f:
                        content = f.read()

                    processed_text = self._process_text(content)

                    new_document = Document(name=file, topic=topic, path=directory)
                    new_document.set_content(content)
                    new_document.set_content_preprocessed(processed_text)

                    self.documents.append(new_document)

            return True
        else:
            return False


    def _process_text(self, txt: str) -> list:

        processed_text = self._text_processor.process_text(text=txt)
        return processed_text
