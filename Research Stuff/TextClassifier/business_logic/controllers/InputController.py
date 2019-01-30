from tkinter import filedialog
from os.path import splitdrive, split
from ui import InputGUI
from business_logic.Readers.IReader import IReader


class InputController:

    def __init__(self, input_gui: InputGUI, reader: IReader):

        # Class members
        self.input_gui = input_gui
        self.reader = reader

        # Operations
        self.input_gui.set_button_commands(self)

        self.input_gui.display()

    def add_directory(self):
        """
        Add directory and topic to the corresponding model. The path is split so that
        the name of the directory is the topic of that directory.
        """
        filename = filedialog.askdirectory(initialdir=".")

        # https://stackoverflow.com/questions/3167154/how-to-split-a-dos-path-into-its-components-in-python
        if not filename:
            print("No file was selected")
        else:
            drive, path_and_file = splitdrive(filename)
            path, file = split(path_and_file)

            self.input_gui.add_new_directory(path=filename, topic=file)
            self.reader.add_path(filename, file)
