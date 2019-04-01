from user_interfaces.IGUI import GUI


class DataRetriever:

    def __init__(self, gui: GUI):
        self.__gui = gui

    def get_text(self):
        return self.__gui.get_unseen_text()

    def get_word(self):
        return self.__gui.get_word()