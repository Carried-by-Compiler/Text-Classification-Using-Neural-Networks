from gensim.models.doc2vec import TaggedDocument


class DataStorer:

    def __init__(self):
        self.__topics = list()
        self.__loaded_topics = list()
        self.__documents = list()

    def add_topic(self, t: str):
        if t not in self.__topics:
            self.__topics.append(t)

    def get_topics(self):
        return self.__topics

    def get_topic_vector(self, t: str):
        topic_vec = list()
        for topic in self.__topics:
            if t == topic:
                topic_vec.append(1)
            else:
                topic_vec.append(0)

        return topic_vec

    def add_loaded_topic(self, topic):
        self.__loaded_topics.append(topic)

    def convert_loaded_topics_to_vecs(self):
        """
        Convert the loaded topics to its one-hot vector representation
        :return:
        """
        for i in range(len(self.__loaded_topics)):
            self.__loaded_topics[i] = self.get_topic_vector(self.__loaded_topics[i])

    def add_document(self, doc):
        self.__documents.append(doc)

    def clear_topics(self):
        self.__topics.clear()

    def clear_documents(self):
        self.__documents.clear()

    def clear(self):
        self.__topics.clear()
        self.__documents.clear()
        self.__loaded_topics.clear()
