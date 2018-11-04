import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim.models import Word2Vec
from wikipedia import page, search
from FileHandler import FileHandler
from os import path


def get_wiki(title: str):

    titles = search(title)
    wikipage = page(titles[0])

    return wikipage


if __name__ == "__main__":

    file_handler = FileHandler()
    corpus = file_handler.get_sentence_processor_iterator()

    model = Word2Vec(corpus, iter=50, min_count=10, size=300, workers=4)

    model.save(path.join(file_handler.model_file_path, "computer_model"))




