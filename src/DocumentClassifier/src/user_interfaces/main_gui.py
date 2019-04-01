# Class imports
from user_interfaces.IGUI import GUI
from business_logic.managers.d2v_manager import D2VManagerStates
from business_logic.managers.d2v_manager import D2VResultKeys
from business_logic.managers.w2v_manager import W2VManagerStates
from business_logic.managers.w2v_manager import W2VResultKeys
from .results_gui import D2VResultsGUI

# Other imports
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from business_logic.invoker import Invoker
from business_logic.managers.observer_dp import Observer
import numpy as np


class UserGUI(GUI, Observer):

    def __init__(self):
        self.__root = Tk()
        self.__root.title("Document Classifier & Word Similarity Tool")
        self.__root.geometry('700x700')
        self.__root.resizable(False, False)

        # Class members/widget
        self.tab = Notebook(master=self.__root)
        self.tab.pack(fill=BOTH, expand=1, padx=15, pady=15)
        self.file_counter = 0

        # Buttons (Doc2Vec)
        self.add_directory = None
        self.add_dataset = None
        self.load_doc2vec_model = None
        self.train_doc2vec = None
        self.train_classifier = None
        self.classify_new_document = None
        self.load_new_document = None

        # Widgets (Doc2Vec)
        self.treeview = None
        self.input_text = None

        # Buttons (Word2Vec)
        self.add_w2v_directory = None
        self.train_word2vec = None
        self.search_similar = None

        # Widgets (Word2Vec)
        self.treeview_w2v = None
        self.output_tree = None
        self.in_box = None

        # Operations
        self.__root.lift()
        self.__init_doc2vec_components()
        self.__init_word2vec_components()

    def __init_doc2vec_components(self):
        doc2vec_frame = Frame()
        doc2vec_frame.pack()
        self.tab.add(doc2vec_frame, text="Doc2Vec")

        # region Top Frame
        top_frame = Frame(master=doc2vec_frame)
        top_frame.pack(fill=X, padx=15, pady=20)
        m = "Please provide the file path to the directories containing the training documents. " \
            "The name of the directory will be the TOPIC/SUBJECT associated with the documents " \
            "contained within that directory."
        message = Message(master=top_frame, text=m, relief="raised")
        message.bind("<Configure>", lambda event: event.widget.configure(width=event.width - 8))
        message.pack(fill=X)
        # endregion

        # region Middle Frame
        training_frame = LabelFrame(master=doc2vec_frame, text="Training")
        training_frame.pack(fill=X, padx=15)
        middle_frame = Frame(master=training_frame)
        middle_frame.pack(fill=BOTH, padx=10, pady=5)

        # Construct the tree view
        # https://stackoverflow.com/questions/22456445/how-to-imitate-this-table-using-tkinter
        self.treeview = Treeview(master=middle_frame)
        self.treeview['columns'] = "topic"
        self.treeview.heading("#0", text="File Path")
        self.treeview.column("#0", anchor="center")
        self.treeview.heading("topic", text="Topic/Subject")
        self.treeview.column("topic", anchor="center")
        self.treeview.pack(fill=X, side=LEFT, expand=1)

        vsb = Scrollbar(master=middle_frame, orient="vertical", command=self.treeview.yview)
        vsb.pack(side=RIGHT, fill=Y)
        self.treeview.configure(yscrollcommand=vsb.set)

        button_frame = Frame(master=training_frame)
        button_frame.pack(padx=10, pady=10, fill=X, expand=0)
        button_in_frame = LabelFrame(master=button_frame, text="Step 1. Initialize Doc2Vec model")
        button_in_frame.pack(side=LEFT, padx=10, pady=5)
        button_train_frame = LabelFrame(master=button_frame, text="Step 2. Train Doc2Vec and Classifier")
        button_train_frame.pack(side=LEFT, padx=10, pady=5)

        self.add_directory = Button(master=button_in_frame, text="Add directory")
        self.add_dataset = Button(master=button_in_frame, text="Add dataset")
        self.load_doc2vec_model = Button(master=button_in_frame, text="Load Doc2Vec model")
        self.train_doc2vec = Button(master=button_train_frame, state=DISABLED, text="Train Doc2Vec")
        self.train_classifier = Button(master=button_train_frame, state=DISABLED, text="Train Classifier")

        self.add_directory.pack(side=LEFT, pady=5, padx=5)
        self.add_dataset.pack(side=LEFT, pady=5, padx=5)
        self.load_doc2vec_model.pack(side=LEFT, pady=5, padx=5)
        self.train_doc2vec.pack(side=LEFT, pady=5, padx=5)
        self.train_classifier.pack(side=LEFT, pady=5, padx=5)
        # endregion

        # region Bottom Frame
        c_doc_frame = LabelFrame(master=doc2vec_frame, text="Document Classification")
        c_doc_frame.pack(fill=X, padx=15, pady=15)

        self.input_text = Text(master=c_doc_frame, height=5)
        self.input_text.pack(fill=X, padx=10, pady=10)

        c_doc_button_frame = Frame(master=c_doc_frame)
        c_doc_button_frame.pack(padx=10, pady=10, fill=X, expand=0)

        self.classify_new_document = Button(master=c_doc_button_frame, text="Classify")
        self.classify_new_document.pack(side=LEFT)
        # endregion

    def __init_word2vec_components(self):
        word2vec_frame = Frame()
        word2vec_frame.pack()
        self.tab.add(word2vec_frame, text="Word2Vec")

        # region Top Frame
        top_frame = Frame(master=word2vec_frame)
        top_frame.pack(fill=X, padx=15, pady=20)

        m = "Please provide the directory containing the document(s) you wish to use for this Word2Vec demonstration." \
            "This program will display words contained in the provided documents that share similar meaning to your input word."
        message = Message(master=top_frame, text=m, relief="raised")
        message.bind("<Configure>", lambda event: event.widget.configure(width=event.width - 8))
        message.pack(fill=X)
        # endregion

        # region Middle Frame
        training_frame = LabelFrame(master=word2vec_frame, text="Training")
        training_frame.pack(fill=X, padx=15)
        middle_frame = Frame(master=training_frame)
        middle_frame.pack(fill=BOTH, padx=10, pady=5, side=LEFT, expand=1)

        self.treeview_w2v = Treeview(master=middle_frame)
        self.treeview_w2v.heading("#0", text="File Name")
        self.treeview_w2v.column("#0", anchor="center")
        self.treeview_w2v.pack(fill=X, side=LEFT, expand=1)

        vsb = Scrollbar(master=middle_frame, orient="vertical", command=self.treeview_w2v.yview)
        vsb.pack(side=RIGHT, fill=Y)
        self.treeview_w2v.configure(yscrollcommand=vsb.set)

        input_button_frame = Frame(master=training_frame)
        input_button_frame.pack(side=LEFT, padx=45, pady=10)

        self.add_w2v_directory = Button(master=input_button_frame, text="Select Directory")
        self.add_w2v_directory.pack()
        self.train_word2vec = Button(master=input_button_frame, text="Train Word2Vec")
        self.train_word2vec.pack(pady=10)
        # endregion

        # region Bottom Frame
        rel_word_frame = LabelFrame(master=word2vec_frame, text="Related Words")
        rel_word_frame.pack(fill=X, padx=15, pady=15)

        input_frame = Frame(master=rel_word_frame)
        input_frame.pack(fill=X, padx=10, pady=10)

        in_label = Label(master=input_frame, text="Enter a word: ")
        in_label.pack(side=LEFT)

        self.in_box = Entry(master=input_frame)
        self.in_box.pack(side=LEFT, padx=5)

        self.search_similar = Button(master=input_frame, state=DISABLED, text="Submit")
        self.search_similar.pack(side=LEFT)

        output_frame = Frame(master=rel_word_frame)
        output_frame.pack(fill=BOTH, padx=10, pady=10)

        self.output_tree = Treeview(master=output_frame)
        self.output_tree['columns'] = "cosine"
        self.output_tree.heading("#0", text="Similar Words")
        self.output_tree.column("#0", anchor="center")
        self.output_tree.heading("cosine", text="Cosine Similarity / Degree of Similarity")
        self.output_tree.column("cosine", anchor="center")

        self.output_tree.pack(fill=X, side=LEFT, expand=1)

        output_vsb = Scrollbar(master=output_frame, orient="vertical", command=self.output_tree.yview)
        output_vsb.pack(side=RIGHT, fill=Y)
        self.output_tree.configure(yscrollcommand=output_vsb.set)
        # endregion

    def set_button_commands(self, button_listener: Invoker):
        """
        Sets the listener for button events.
        :param button_listener: The object that will handle the button presses.
        :return: None
        """
        self.add_directory.configure(command=button_listener.add_directory_doc2vec)
        self.add_dataset.configure(command=button_listener.add_dataset_doc2vec)
        self.load_doc2vec_model.configure(command=button_listener.load_doc2vec)
        self.train_doc2vec.configure(command=button_listener.train_doc2vec)
        self.train_classifier.configure(command=button_listener.train_classifier)
        self.classify_new_document.configure(command=button_listener.classify_doc)
        self.add_w2v_directory.configure(command=button_listener.add_word2vec_folder)
        self.train_word2vec.configure(command=button_listener.train_word2vec)
        self.search_similar.configure(command=button_listener.search_similar_words)

    def get_unseen_text(self):
        return self.input_text.get("1.0", "end-1c")

    def get_word(self):
        return self.in_box.get()

    def display(self):
        self.__root.mainloop()

    def update(self, args):
        state = args[D2VResultKeys.STATE]

        if state == D2VManagerStates.ADD_DIR:
            self.__output_selected_directory(p=args[D2VResultKeys.FILE_PATH], topic=args[D2VResultKeys.TOPIC],
                                             files=args[D2VResultKeys.FILES])
            self.train_doc2vec["state"] = "normal"
        elif state == D2VManagerStates.ADD_DATASET:
            self.__display_dataset()
        elif state == D2VManagerStates.LOAD_MODEL:
            self.__model_loaded(args[D2VResultKeys.TOPICS])
        elif state == D2VManagerStates.TRAIN_D2V_STATUS:
            if args[D2VResultKeys.STATUS] == "SUCCESS":
                self.__display_d2v_training_status(1)
            elif args[D2VResultKeys.STATUS] == "ERROR":
                self.__display_d2v_training_status(2)
        elif state == D2VManagerStates.TRAIN_CLASSIFIER:
            messagebox.showinfo("Training Complete", "Successfully trained classifier")
        elif state == D2VManagerStates.CLASSIFIER_RESULT:
            self.__output_results(args[D2VResultKeys.TOPICS], args[D2VResultKeys.RESULTS])
        elif state == W2VManagerStates.W2V_FILES:
            self.__display_w2v_directory(args[W2VResultKeys.FILES])
        elif state == W2VManagerStates.TRAIN_W2V_STATUS:
            if args[W2VResultKeys.STATUS] == "SUCCESS":
                self.__display_w2v_training_status(1)
            elif args[W2VResultKeys.STATUS] == "ERROR":
                self.__display_w2v_training_status(2)
        elif state == W2VManagerStates.SIMILAR_WORDS:
            self.__display_similar_words(args[W2VResultKeys.WORDS])
        else:
            print("main_gui: Invalid state passed!")

    def __display_dataset(self):
        self.train_doc2vec["state"] = "normal"
        self.file_counter = 0
        self.treeview.delete(*self.treeview.get_children())

    def __model_loaded(self, topics):
        self.train_classifier["state"] = "normal"
        self.add_dataset["state"] = "disabled"
        self.add_directory["state"] = "disabled"
        self.treeview.delete(*self.treeview.get_children())
        self.__display_topics(topics)

    def __display_d2v_training_status(self, status):
        if status == 1:
            messagebox.showinfo("Training Complete", "Successfully trained doc2vec model")
            self.train_classifier["state"] = "normal"
            self.train_doc2vec["state"] = "disabled"
        elif status == 2:
            messagebox.showinfo("Training Failed", "An error occurred during doc2vec training")

    def __display_w2v_training_status(self, status):
        if status == 1:
            messagebox.showinfo("Training Complete", "Successfully trained word2vec model")
            self.search_similar["state"] = "normal"
        elif status == 2:
            messagebox.showinfo("Training Failed", "An error occurred during word2vec training")

    def __display_similar_words(self, result):
        self.output_tree.delete(*self.output_tree.get_children())
        if type(result) is list:

            if len(result) is not None:
                for i, r in enumerate(result):
                    word = r[0]
                    cosine = r[1]
                    self.output_tree.insert("", "end", iid=i, text=word, values=cosine)
        else:
            self.output_tree.insert("", "end", iid=0, text="Word doesn't exist in vocab", values="N/A")

    def __display_topics(self, topics):
        self.treeview.delete(*self.treeview.get_children())

        for i, topic in enumerate(topics):
            self.treeview.insert("", "end", iid=i, text="Loaded documents", values=topic)

    def __output_selected_directory(self, p, topic, files):
        self.file_counter = self.file_counter + 1

        self.treeview.insert("", "end", iid=self.file_counter, text=p, values=topic)
        if len(files) is not None:
            for file in files:
                self.treeview.insert(self.file_counter, "end", text=file, values=topic)

    def __display_w2v_directory(self, files):
        self.treeview_w2v.delete(*self.treeview_w2v.get_children())
        for i in range(len(files)):
            self.treeview_w2v.insert("", "end", iid=i, text=files[i])

    def __output_results(self, topics, results):
        results_gui = D2VResultsGUI()
        results_gui.display_results(topics, results)
        results_gui.display()
