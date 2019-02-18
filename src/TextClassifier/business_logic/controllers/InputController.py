from tkinter import filedialog, messagebox
from os.path import splitdrive, split
from ui import InputGUI
from business_logic.readers.IReader import IReader
from business_logic.Doc2Vec import D2V
from business_logic.classifiers.NeuralNetwork import NeuralNetwork
from business_logic.DataStorer import DataStorer
import numpy as np


class InputController:

    def __init__(self, input_gui: InputGUI, reader: IReader):

        # Class members
        self.__input_gui = input_gui
        self.__reader = reader

        self.__d2v = D2V() # TODO: create a factory method to choose object
        self.__classifier = NeuralNetwork()  # TODO: create a factory method to choose classifier
        self.__data_store = DataStorer()

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

            print(filename)

            files = self.__reader.add_path(filename, file, self.__data_store)
            if len(files) != 0:
                self.__input_gui.add_new_directory(path=filename, topic=file, files=files)
                self.__input_gui.enable_training_button()
    """
    def confirm_selection(self):

        try:

            self.__tagged_documents = list(self.__reader.load_documents())

            if self.__tagged_documents[0] is False:
                messagebox.showwarning("No Documents", "You have not added any directories!")
            else:
                messagebox.showinfo("Loaded Documents", "Successfully loaded documents")
                self.__input_gui.enable_training_button()

        except Exception as e:
            messagebox.showerror("Loading Documents Error", str(e))
    """
    def start_d2v(self):
        val = self.__d2v.train_model(self.__data_store)
        if val == 1:
            messagebox.showinfo("Training Complete", "Successfully trained doc2vec model")
            self.__input_gui.enable_classification_button()

    def start_classification(self):

        documents = self.__data_store.get_documents()
        docs = list()
        topics = list()

        for doc in documents:
            docs.append(self.__d2v.get_doc_vec(doc.get_id()))
            topics.append(self.__data_store.get_topic_vector(doc.get_topic()))

        self.__classifier.train(np.array(docs, ndmin=2), np.array(topics, ndmin=2))
        print("Classifier trained!")

    def process_new_document(self):
        content = self.__input_gui.get_new_document()
        processed_content = self.__reader.process_text(txt=content)

        new_doc = self.__d2v.infer_new_document(processed_content)
        #  new_doc = self.__d2v.infer(processed_content)
        print("New doc: %s" % new_doc)
        #  self.__d2v.get_similar(new_doc)

        results = self.__classifier.predict(x=new_doc)

        print(self.__data_store.get_topics())
        print(results)

        self.__input_gui.output_results(self.__data_store.get_topics(), results)
