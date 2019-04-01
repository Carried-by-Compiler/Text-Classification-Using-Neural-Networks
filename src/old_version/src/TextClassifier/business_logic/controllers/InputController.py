from tkinter import filedialog, messagebox
import os
from ui import InputGUI
from business_logic.readers.IReader import IReader
from business_logic.Doc2Vec import D2V
from business_logic.Word2Vec import W2V
from business_logic.classifiers.NeuralNetwork import NeuralNetwork
from business_logic.DataStorer import DataStorer
from business_logic.w2v_helper import Word2VecHelper
import numpy as np


class InputController:

    def __init__(self, input_gui: InputGUI, reader: IReader):

        # Class members
        self.__input_gui = input_gui
        self.__reader = reader

        self.__d2v = D2V()  # TODO: create a factory method to choose object
        self.__w2v = W2V()
        self.__w2v_helper = Word2VecHelper()
        self.__data_store = DataStorer()
        self.__classifier = NeuralNetwork()  # TODO: create a factory method to choose classifier

        self.__loaded_topics = list()

        # Operations
        self.__input_gui.set_button_commands(self)
        self.__input_gui.display()

    def add_directory(self):
        """
        Add directory and topic to the corresponding model. The path is split so that
        the name of the directory is the topic of that directory.
        """
        self.__input_gui.disable_load_doc2vec()
        filename = filedialog.askdirectory(initialdir=".")

        # https://stackoverflow.com/questions/3167154/how-to-split-a-dos-path-into-its-components-in-python
        if not filename:
            print("No file was selected")
        else:
            drive, path_and_file = os.path.splitdrive(filename)
            path, file = os.path.split(path_and_file)

            print(filename)

            files = self.__reader.add_path(filename, file, self.__data_store)
            if len(files) != 0:
                self.__input_gui.add_new_directory(path=filename, topic=file, files=files)
                self.__input_gui.enable_training_button()

    def add_w2v_directory(self):
        filename = filedialog.askdirectory(initialdir=".")
        if not filename:
            print("No file was selected")
        else:
            files = os.listdir(filename)
            if len(files) != 0:
                self.__input_gui.add_w2v_files(files)
                self.__w2v_helper.set_path(p=filename)
                self.__w2v.refresh()
            else:
                print("No files in directory")

    def start_w2v(self):
        self.__w2v.train_model(self.__w2v_helper)

    def search_similar_words(self):
        word = self.__input_gui.get_w2v_input()
        try:
            similarity = self.__w2v.get_similar_words(word=word)
        except KeyError as e:
            print(e)
            similarity = ""
        self.__input_gui.display_similarity(similarity)

    def start_d2v(self):
        val = self.__d2v.train_model(self.__data_store)
        if val == 1:
            # self.__d2v.save_model("D:\\workspace\\Text-Classification-Using-Neural-Networks\\src\\TextClassifier\\doc2vec_models\\epochs100vector300.d2v")
            messagebox.showinfo("Training Complete", "Successfully trained doc2vec model")
            self.__input_gui.enable_classification_button(self, 0)

    def load_d2v(self):
        model_path = filedialog.askopenfilename(initialdir="./doc2vec_models", title="Select Doc2Vec model",
                                                filetypes=(("Doc2Vec Models", "*.d2v"), ("All Files", "*")))
        self.__d2v.load_model(model_path)
        self.__load_data()
        self.__display_topics()
        self.__input_gui.disable_add_directory()
        # self.__input_gui.disable_add_dataset()
        self.__input_gui.enable_classification_button(self, 1)

    def __load_data(self):
        labels = self.__d2v.get_labels()

        for label in labels:
            self.__data_store.add_document(self.__d2v.get_doc_vec(label))
            split_string = label.split("__")
            self.__loaded_topics.append(split_string[0])
            self.__data_store.add_topic(split_string[0])

    def __display_topics(self):
        self.__input_gui.display_topics(self.__data_store.get_topics())

    def start_classification(self):

        docs = list()
        topics = list()

        documents = self.__data_store.get_documents()

        for doc in documents:
            docs.append(self.__d2v.get_doc_vec(doc.get_id()))
            topics.append(self.__data_store.get_topic_vector(doc.get_topic()))

        self.__classifier.train(np.array(docs, ndmin=2), np.array(topics, ndmin=2))
        print("Classifier trained!")

    def start_classification_loaded(self):

        # Convert topic in topics list to its vector representation
        for i in range(len(self.__loaded_topics)):
            self.__loaded_topics[i] = self.__data_store.get_topic_vector(self.__loaded_topics[i])

        self.__classifier.train(np.array(self.__data_store.get_documents(), ndmin=2),
                                np.array(self.__loaded_topics, ndmin=2))
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
