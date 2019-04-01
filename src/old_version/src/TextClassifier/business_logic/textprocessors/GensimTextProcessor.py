from gensim.utils import simple_preprocess
import numpy
from .ITextProcessor import ITextProcessor


class GensimTextProcessor(ITextProcessor):
    """
    Class that uses Gensim's simple_preprocess function to
    process text.
    """

    def process_text(self, text: str) -> numpy.array:
        return simple_preprocess(text)
