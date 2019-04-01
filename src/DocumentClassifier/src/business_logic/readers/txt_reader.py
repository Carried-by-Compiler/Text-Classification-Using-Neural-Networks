from business_logic.readers.reader import Reader
from business_logic.text_processors.processor_factory import ProcessorFactory
from os import listdir, path
from gensim.models.doc2vec import TaggedDocument


class TxtReader(Reader):

    def __init__(self, manager_type):
        if manager_type == "D2V":
            self.__file_paths = list()
        elif manager_type == "W2V":
            self.__file_paths = str()
        self.__text_processor = ProcessorFactory.create_processor("GENSIM")

    def add_path(self, file_path):
        if isinstance(self.__file_paths, list):
            self.__file_paths.append(file_path)
        elif isinstance(self.__file_paths, str):
            self.__file_paths = file_path
        print("TxtReader: current file_path status: " + str(self.__file_paths))
        files = listdir(file_path)
        return files

    def clear_paths(self):
        self.__file_paths.clear()

    @staticmethod
    def read_file(file_path):
        with open(file_path, mode="r", encoding="utf-8") as f:
            content = f.read()

        return content

    def yield_documents(self):

        if not self.__file_paths:
            print("TxtReader: No paths saved")
        else:
            for f_path in self.__file_paths:

                path_split = f_path.split("/")
                topic = path_split[len(path_split) - 1]
                files = listdir(f_path)
                print("TxtReader: Processing files in topic: " + topic)
                for i, file in enumerate(files):
                    full_path = path.join(f_path, file)
                    file_content = self.read_file(full_path)
                    content_preprocessed = self.__text_processor.process_text(file_content)
                    label = topic + "__" + str(i)

                    yield TaggedDocument(content_preprocessed, [label])
        return

    def yield_line(self):
        files = listdir(self.__file_paths)
        for file in files:
            for line in open(path.join(self.__file_paths, file), "r", encoding="utf-8"):
                yield self.__text_processor.process_text(line)

    def process_text(self, text):
        return self.__text_processor.process_text(text)



