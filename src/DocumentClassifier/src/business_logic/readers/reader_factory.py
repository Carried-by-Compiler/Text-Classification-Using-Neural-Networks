from .txt_reader import TxtReader
from .reader import Reader


class ReaderFactory:

    TEXT = "TEXT"

    @staticmethod
    def create_reader(reader_type: str, manager_type: str) -> Reader:
        reader = None

        if reader_type == 'TEXT':
            reader = TxtReader(manager_type)

        return reader
