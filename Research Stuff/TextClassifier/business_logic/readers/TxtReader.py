from business_logic.readers.IReader import IReader
from business_logic.textprocessors.GensimTextProcessor import GensimTextProcessor
from business_logic.models.Document import Document
from gensim.models.doc2vec import TaggedDocument
from business_logic.DataStorer import DataStorer
from os import listdir, path


class TxtReader(IReader):
    """
    This class is used to read documents of txt file format. It also
    stores the topics associated with each file path
    """

    def remove_path(self, directory: str, data_store: DataStorer):
        pass

    def print_paths(self, data_store: DataStorer):
        pass

    def __init__(self):

        # TODO: try to use factory method here
        self.__text_processor = GensimTextProcessor()

    def add_path(self, directory_path: str, topic: str, data_store: DataStorer) -> list:
        """
        Adds files belonging to a directory into the program.

        :param directory_path: The directory path to the file
        :param topic: The topic associated with the directory
        :param data_store: A data store object to store the files
        :return: A list of the file names in that directory
        """

        files = []

        if data_store.check_topic_exists(topic) is True:
            print("TxtReader: File has already been added!")
        else:
            data_store.add_topic(t=topic)

            files = listdir(directory_path)
            print("Adding %s files" % topic) # TODO: remove print

            for i, file in enumerate(files):

                full_path = path.join(directory_path, file)
                file_content = self.__read_file(file_path=full_path)
                processed_text = self.__text_processor.process_text(file_content)

                new_doc = Document(name=file, topic=topic, path=directory_path)
                new_doc.set_id(counter=i)
                new_doc.set_content(content=file_content)
                new_doc.set_content_preprocessed(content=processed_text)

                data_store.add_document(new_doc)
                print("Added document: %s\nID: %s\n" % (new_doc.get_name(), new_doc.get_id()))  # TODO: remove print

        return files

    def __read_file(self, file_path: str) -> str:
        with open(file_path, mode="r", encoding="utf-8") as f:
            content = f.read()

        return content

    def clear_paths(self):
        self.__paths.clear()

    def process_text(self, txt: str) -> list:

        processed_text = self.__text_processor.process_text(text=txt)
        return processed_text

    def get_document(self, identifier: int) -> Document:
        """
        Get a specific document
        :param identifier: The ID of the document
        :return: The document object
        """

        document = None

        for doc in self.__documents:
            if doc.get_id() == identifier:
                document = doc
                break

        return document
