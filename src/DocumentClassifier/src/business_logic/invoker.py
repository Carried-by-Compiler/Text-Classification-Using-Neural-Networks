class Invoker:

    def __init__(self):
        self.__commands = dict()

    def store_command(self, name, command):
        self.__commands[name] = command

    def add_directory_doc2vec(self):
        """
        Triggers the action to add a file path to a directory.
        :return: None
        """
        command = self.__commands["ADD_DIR_D2V"]
        command.execute()

    def add_dataset_doc2vec(self):
        command = self.__commands["ADD_DATASET_D2V"]
        command.execute()

    def load_doc2vec(self):
        command = self.__commands["LOAD_D2V"]
        command.execute()

    def train_doc2vec(self):
        command = self.__commands["TRAIN_D2V"]
        command.execute()

    def train_classifier(self):
        command = self.__commands["TRAIN_CLASSIFIER"]
        command.execute()

    def classify_doc(self):
        command = self.__commands["CLASSIFY"]
        command.execute()

    def add_word2vec_folder(self):
        command = self.__commands["ADD_FOLDER"]
        command.execute()

    def train_word2vec(self):
        command = self.__commands["TRAIN_W2V"]
        command.execute()

    def search_similar_words(self):
        command = self.__commands["SIMILAR_WORDS"]
        command.execute()
