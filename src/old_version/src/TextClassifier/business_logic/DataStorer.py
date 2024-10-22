from gensim.models.doc2vec import TaggedDocument
from business_logic.models.Document import Document


class DataStorer:

    def __init__(self):
        self.__topics = list()
        self.__documents = list()

    def __iter__(self):
        for doc in self.__documents:
            yield TaggedDocument(doc.get_content_preprocessed(), [doc.get_id()])

    def add_topic(self, t: str):
        if t not in self.__topics:
            self.__topics.append(t)

    def get_topic_vector(self, t: str):
        topic_vec = list()
        for topic in self.__topics:
            if t == topic:
                topic_vec.append(1)
            else:
                topic_vec.append(0)

        return topic_vec

    def check_topic_exists(self, t: str) -> bool:
        exists = False

        for topic in self.__topics:
            if t == topic:
                exists = True
                break

        return exists

    def get_topics(self):
        return self.__topics

    def add_document(self, doc):
        self.__documents.append(doc)

    def get_documents(self):
        return self.__documents

    def clear(self):
        self.__topics.clear()
        self.__documents.clear()

    def print_docs(self):
        for i, doc in enumerate(self.__documents):
            print("# %d\ndoc: %s\ntopic: %s\ncontent: %s\n" % (i, doc.get_name(), doc.get_topic(), doc.get_content_preprocessed()))