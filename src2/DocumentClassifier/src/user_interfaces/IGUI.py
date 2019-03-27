import abc


class GUI(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_file_paths(self): pass

    @abc.abstractmethod
    def get_unseen_text(self): pass

    @abc.abstractmethod
    def get_unseen_file_path(self): pass
