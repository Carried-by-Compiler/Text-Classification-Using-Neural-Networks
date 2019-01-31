from tkinter import filedialog, messagebox
from os.path import splitdrive, split
from ui import InputGUI
from business_logic.readers.IReader import IReader
from business_logic.Doc2Vec import D2V


class InputController:

    def __init__(self, input_gui: InputGUI, reader: IReader):

        # Class members
        self.__input_gui = input_gui
        self.__reader = reader

        self.__d2v = D2V()
        self.__tagged_documents = None

        # Operations
        self.__input_gui.set_button_commands(self)

        self.__input_gui.display()

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

            files = self.__reader.add_path(filename, file)
            if len(files) != 0:
                self.__input_gui.add_new_directory(path=filename, topic=file, files=files)

    def confirm_selection(self):

        try:

            self.__tagged_documents = list(self.__reader.load_documents())
            print(self.__tagged_documents[0])
            if self.__tagged_documents[0] is False:
                messagebox.showwarning("No Documents", "You have not added any directories!")
            else:
                messagebox.showinfo("Loaded Documents", "Successfully loaded documents")
                self.__input_gui.enable_training_button()

        except BaseException:
            messagebox.showerror("Loading Documents Error", "Error occurred while loading documents")

    def start_d2v(self):
        val = self.__d2v.train_model(self.__tagged_documents)
        if val == 1:
            messagebox.showinfo("Training Complete", "Successfully trained doc2vec model")