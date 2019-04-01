from os import listdir, path
from gensim.utils import simple_preprocess


class Word2VecHelper:

    def __init__(self):
        self.__file_path = ""

    def __iter__(self):
        files = listdir(self.__file_path)

        for file in files:
            for line in open(path.join(self.__file_path, file), "r", encoding="utf-8"):
                yield simple_preprocess(line)

    def set_path(self, p: str):
        self.__file_path = p
