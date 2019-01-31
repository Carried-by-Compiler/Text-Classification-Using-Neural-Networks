import abc


class IReader(metaclass=abc.ABCMeta):
    """
    Interface for all classes wishing to store and read documents
    """

    @abc.abstractmethod
    def add_path(self, directory: str, topic: str):
        pass

    @abc.abstractmethod
    def remove_path(self, directory: str):
        pass

    @abc.abstractmethod
    def print_paths(self):
        pass

    @abc.abstractmethod
    def clear_paths(self):
        pass

    @abc.abstractmethod
    def load_documents(self):
        pass
