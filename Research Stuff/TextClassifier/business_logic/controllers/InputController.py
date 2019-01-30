from tkinter import filedialog
from os.path import splitdrive, split

class InputController:

    def __init__(self, input_gui, reader):

        # Class members
        self.input_gui = input_gui
        self.reader = reader

        # Operations
        self.input_gui.set_button_commands(self)

        self.input_gui.display()

    def add_directory(self):
        filename = filedialog.askdirectory(initialdir=".")

        # https://stackoverflow.com/questions/3167154/how-to-split-a-dos-path-into-its-components-in-python
        if not filename:
            print("No file was selected")
        else:
            drive, path_and_file = splitdrive(filename)
            path, file = split(path_and_file)
            print(file)

            self.input_gui.add_new_directory(path=filename, topic=file)

