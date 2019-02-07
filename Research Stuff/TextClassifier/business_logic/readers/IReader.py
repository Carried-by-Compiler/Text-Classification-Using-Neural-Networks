import abc
from business_logic.DataStorer import DataStorer


class IReader(metaclass=abc.ABCMeta):
    """
    Interface for all classes wishing to store and read documents
    """

    @abc.abstractmethod
    def add_path(self, directory_path: str, topic: str, data_store: DataStorer):
        pass

    @abc.abstractmethod
    def remove_path(self, directory: str, data_store: DataStorer):
        pass

    @abc.abstractmethod
    def print_paths(self, data_store: DataStorer):
        pass
