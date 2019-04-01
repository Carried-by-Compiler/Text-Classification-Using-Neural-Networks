import abc


class Reader(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def add_path(self, file_path): pass

    @abc.abstractmethod
    def clear_paths(self): pass

    @abc.abstractmethod
    def process_text(self, text): pass

    @abc.abstractmethod
    def yield_line(self): pass

    @abc.abstractmethod
    def yield_documents(self): pass
