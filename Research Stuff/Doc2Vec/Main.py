import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from DataSetBuilder import DataSetBuilder
from FileHandler import FileHandler
import gensim


def fill_data(name=""):
    db_builder = DataSetBuilder()
    db_builder.fill("Computer")


def make_file(name, folder):
    db_builder = DataSetBuilder()
    db_builder.make_file(name, folder)


if __name__ == "__main__":
    """
    make_file("William Shakespeare", "Literature")
    """

    file_handler = FileHandler()
    file_handler.update_path(folder="Literature")
    model = gensim.models.Doc2Vec.load(file_handler.get_models_folder() + "\\exampleEPOCH600.d2v")
    document = file_handler.read_preprocessed("William Shakespeare.txt")
    new_document = model.infer_vector(document)
    print(model.docvecs.most_similar([new_document]))
    #print(model.docvecs.most_similar(positive=document))



"""
    # Building the Doc2Vec model
    file_handler = FileHandler()
    file_handler.update_path("All")
    documents = list(file_handler.read_corpus())
    
    model = gensim.models.Doc2Vec(vector_size=3, min_count=2, epochs=600)
    model.build_vocab(documents)
    model.train(documents, total_examples=model.corpus_count, epochs=model.epochs)
    model.save(file_handler.get_models_folder() + "\\exampleEPOCH600.d2v")
"""


