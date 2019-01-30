from business_logic.Readers.IReader import IReader


class TxtReader(IReader):
    """
    This class is used to read documents of txt file format. It also
    stores the topics associated with each file path
    """

    def __init__(self):
        self.paths = {}

    def add_path(self, directory: str, topic: str):
        self.paths[directory] = topic

    def remove_path(self, directory: str):
        del self.paths[directory]

    def print_paths(self):
        for d in self.paths:
            print(d, "=>", self.paths[d])

    def clear_paths(self):
        self.paths.clear()
