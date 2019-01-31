from tkinter import filedialog, messagebox
from os.path import splitdrive, split
from ui import InputGUI
from business_logic.readers.IReader import IReader


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

            files = self.reader.add_path(filename, file)
            if len(files) != 0:
                self.input_gui.add_new_directory(path=filename, topic=file, files=files)

    def confirm_selection(self):
        try:

            if self.reader.load_documents() is True:
                messagebox.showinfo("Loaded Documents", "Successfully loaded documents")
                self.input_gui.enable_training_button()
            else:
                messagebox.showwarning("No Documents", "You have not added any directories!")
        except BaseException:
            messagebox.showerror("Loading Documents Error", "Error occurred while loading documents")
