from business_logic.commands.command import Command


class AddDirectoryCommand(Command):

    def __init__(self, receiver):
        self.__receiver = receiver

    def execute(self):
        self.__receiver.add_directory()


class AddDatasetCommand(Command):

    def __init__(self, receiver):
        self.__receiver = receiver

    def execute(self):
        self.__receiver.add_dataset()


class LoadModelCommand(Command):

    def __init__(self, receiver):
        self.__receiver = receiver

    def execute(self):
        self.__receiver.load_model()


class TrainDoc2VecCommand(Command):

    def __init__(self, receiver):
        self.__receiver = receiver

    def execute(self):
        self.__receiver.train_doc2vec()


class TrainClassifierCommand(Command):

    def __init__(self, receiver):
        self.__receiver = receiver

    def execute(self):
        self.__receiver.train_classifier()


class ClassifyDocumentCommand(Command):

    def __init__(self, receiver):
        self.__receiver = receiver

    def execute(self):
        self.__receiver.classify_document()


class AddFolderW2VCommand(Command):

    def __init__(self, receiver):
        self.__receiver = receiver

    def execute(self):
        self.__receiver.add_w2v_folder()


class TrainWord2VecCommand(Command):

    def __init__(self, receiver):
        self.__receiver = receiver

    def execute(self):
        self.__receiver.train_word2vec()


class GetSimilarWordsCommand(Command):

    def __init__(self, receiver):
        self.__receiver = receiver

    def execute(self):
        self.__receiver.find_similar_words()