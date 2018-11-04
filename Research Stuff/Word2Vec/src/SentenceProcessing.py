import os
from gensim.utils import simple_preprocess
import logging


class SentenceProcessor:
    """
    This class handles file reading. It is capable of parsing sentences
    from multiple files in a directory
    """

    def __init__(self, directory):
        """
        Initialize SentenceProcessor object

        :param directory: the file path to a directory containing the files to be read
        """
        self.directory = directory

    def __iter__(self):
        """
        :return: an iterable object representing a line of a file that is
                 processed and split up
        """
        for file_name in os.listdir(self.directory):
            for line in open(os.path.join(self.directory, file_name), "r", encoding="utf-8"):
                yield simple_preprocess(line)