from gensim.utils import simple_preprocess
from .text_processor import TextProcessor


class GensimTextProcessor(TextProcessor):

    def process_text(self, text):
        return simple_preprocess(text)
