from .gensim_processor import GensimTextProcessor
from .text_processor import TextProcessor


class ProcessorFactory:

    @staticmethod
    def create_processor(processor_type: str) -> TextProcessor:
        processor = None

        if processor_type == "GENSIM":
            processor = GensimTextProcessor()

        return processor
