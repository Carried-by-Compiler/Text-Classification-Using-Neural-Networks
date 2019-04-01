from tkinter import *
from tkinter.ttk import * #Treeview, Notebook, Style
from business_logic.controllers import InputController
from ui.Doc2VecResultsGUI import Doc2VecResultsGUI
import numpy as np
import types


class InputGUI:
    """
    This is the GUI class where the relevant parameters to the program
    is provided from the end user.

    Possible input parameters include:
    - File path to the training documents
    - The topic of the training documents
    - The document to classify
    - Parameters to Doc2Vec/Word2Vec models
    - Parameters to classification model
    """

    def __init__(self):
        self.root = Tk()
        self.root.title("Document Classifier")
        self.root.geometry('700x700')
        self.root.resizable(False, False)

        # CLASS MEMBERS

        # Buttons (Doc2Vec)
        self.add_button = None
        self.start_doc2vec = None
        self.load_doc2vec = None
        self.start_classification = None
        self.add_doc = None
        self.classify_doc = None
        self.load_unseen_doc = None
        self.add_dataset = None

        # Other Widgets (Doc2Vec)
        self.message = None
        self.treeview = None
        self.tab = None
        self.input_text = None
        self.file_counter = 0

        # Buttons (Word2Vec)
        self.add_in_directory = None
        self.train_word2vec = None
        self.search_similar = None

        # Other Widgets (Word2Vec)
        self.treeview_w2v = None
        self.output_tree = None
        self.in_box = None

        # OPERATIONS
        self.root.lift()
        self.init_components()

    def change(self, event):
        curr_tab = self.tab.tab(self.tab.select(), "text")
        print(curr_tab)

    def init_components(self):
        """
        Initialise and output GUI widgets
        :return:
        """
        self.tab = Notebook(master=self.root)
        self.tab.pack(fill=BOTH, expand=1, padx=15, pady=15)
        self.tab.bind("<<NotebookTabChanged>>", self.change)

        self.init_doc2vec_components()
        self.init_word2vec_components()
        # TODO refactor code for switching between doc2vec and word2vec so that it is cleaner and more maintainable

    def init_doc2vec_components(self):
        doc2vec_frame = Frame()
        doc2vec_frame.pack()
        self.tab.add(doc2vec_frame, text="Doc2Vec")

        # Top Frame
        top_frame = Frame(master=doc2vec_frame)
        top_frame.pack(fill=X, padx=15, pady=20)

        m = "Please provide the file path to the directories containing the training documents. " \
            "The name of the directory will be the TOPIC/SUBJECT associated with the documents " \
            "contained within that directory."
        self.message = Message(master=top_frame, text=m, relief="raised")
        self.message.bind("<Configure>", lambda event: event.widget.configure(width=event.width - 8))
        self.message.pack(fill=X)

        # Middle Frame

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

        button_in_frame = LabelFrame(master=button_frame, text="Step 1. Initialise Doc2Vec model")
        button_in_frame.pack(side=LEFT, padx=10, pady=5)

        button_train_frame = LabelFrame(master=button_frame, text="Step 2. Train Doc2Vec and classifier")
        button_train_frame.pack(side=LEFT, padx=10, pady=5)

        self.add_button = Button(master=button_in_frame, text="Add directory")
        self.add_button.pack(side=LEFT, pady=5, padx=5)
        # self.add_dataset = Button(master=button_in_frame, text="Add dataset")
        # self.add_dataset.pack(side=LEFT, pady=5, padx=5)
        self.load_doc2vec = Button(master=button_in_frame, text="Load Doc2Vec model")
        self.load_doc2vec.pack(side=LEFT, pady=5, padx=5)
        self.start_doc2vec = Button(master=button_train_frame, state=DISABLED, text="Train Doc2Vec")
        self.start_doc2vec.pack(side=LEFT, pady=5, padx=5)
        self.start_classification = Button(master=button_train_frame, state=DISABLED, text="Train Classifier")
        self.start_classification.pack(side=LEFT, pady=5, padx=5)

        c_doc_frame = LabelFrame(master=doc2vec_frame, text="Document Classification")
        c_doc_frame.pack(fill=X, padx=15, pady=15)

        self.input_text = Text(master=c_doc_frame, height=5)
        self.input_text.pack(fill=X, padx=10, pady=10)

        c_doc_button_frame = Frame(master=c_doc_frame)
        c_doc_button_frame.pack(padx=10, pady=10, fill=X, expand=0)

        self.add_doc = Button(master=c_doc_button_frame, text="Classify")
        self.add_doc.pack(side=LEFT)
        # self.load_unseen_doc = Button(master=c_doc_button_frame, text="Load Document")
        # self.load_unseen_doc.pack(side=LEFT)

    def init_word2vec_components(self):
        word2vec_frame = Frame()
        self.tab.add(word2vec_frame, text="Word2Vec")

        # Top Frame
        top_frame = Frame(master=word2vec_frame)
        top_frame.pack(fill=X, padx=15, pady=20)

        """
        m = "Please provide the file path to the directories containing the training documents. " \
            "The name of the directory will be the TOPIC/SUBJECT associated with the documents " \
            "contained within that directory."
        """

        m = "Please provide the directory containing the document(s) you wish to use for this Word2Vec demonstration." \
            "This program will display words contained in the provided documents that share similar meaning to your input word."
        self.message = Message(master=top_frame, text=m, relief="raised")
        self.message.bind("<Configure>", lambda event: event.widget.configure(width=event.width - 8))
        self.message.pack(fill=X)

        # Middle Frame
        training_frame = LabelFrame(master=word2vec_frame, text="Training")
        training_frame.pack(fill=X, padx=15)

        middle_frame = Frame(master=training_frame)
        middle_frame.pack(fill=BOTH, padx=10, pady=5, side=LEFT, expand=1)
        # Construct the tree view
        # https://stackoverflow.com/questions/22456445/how-to-imitate-this-table-using-tkinter
        self.treeview_w2v = Treeview(master=middle_frame)
        self.treeview_w2v.heading("#0", text="File Name")
        self.treeview_w2v.column("#0", anchor="center")

        self.treeview_w2v.pack(fill=X, side=LEFT, expand=1)

        vsb = Scrollbar(master=middle_frame, orient="vertical", command=self.treeview_w2v.yview)
        vsb.pack(side=RIGHT, fill=Y)
        self.treeview_w2v.configure(yscrollcommand=vsb.set)

        input_button_frame = Frame(master=training_frame)
        input_button_frame.pack(side=LEFT, padx=45, pady=10)

        self.add_in_directory = Button(master=input_button_frame, text="Select Directory")
        self.add_in_directory.pack()
        self.train_word2vec = Button(master=input_button_frame, text="Train Word2Vec")
        self.train_word2vec.pack(pady=10)

        rel_word_frame = LabelFrame(master=word2vec_frame, text="Related Words")
        rel_word_frame.pack(fill=X, padx=15, pady=15)

        input_frame = Frame(master=rel_word_frame)
        input_frame.pack(fill=X, padx=10, pady=10)

        in_label = Label(master=input_frame, text="Enter a word: ")
        in_label.pack(side=LEFT)

        self.in_box = Entry(master=input_frame)
        self.in_box.pack(side=LEFT, padx=5)

        self.search_similar = Button(master=input_frame, text="Submit")
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

    def set_button_commands(self, button_listener: InputController):
        """
        Attach button listeners to the button widgets of the window
        :param button_listener: The class that would handle button events.
        """
        self.add_button.configure(command=button_listener.add_directory)
        self.start_doc2vec.configure(command=button_listener.start_d2v)
        self.start_classification.configure(command=button_listener.start_classification)
        self.add_doc.configure(command=button_listener.process_new_document)
        self.load_doc2vec.configure(command=button_listener.load_d2v)

        self.add_in_directory.configure(command=button_listener.add_w2v_directory)
        self.train_word2vec.configure(command=button_listener.start_w2v)
        self.search_similar.configure(command=button_listener.search_similar_words)

    def add_new_directory(self, path: str, topic: str, files: list):
        """
        Output the directory and the corresponding topic to the GUI
        :param path: The file path
        :param topic: The corresponding topic
        :param files: The file names in that directory
        :return:
        """
        self.file_counter = self.file_counter + 1
        self.treeview.insert("", "end", iid=self.file_counter, text=path, values=topic)

        if len(files) is not None:
            for file in files:
                self.treeview.insert(self.file_counter, "end", text=file, values=topic)

    def add_w2v_files(self, files: list):
        self.treeview_w2v.delete(*self.treeview_w2v.get_children())
        for i in range(len(files)):
            self.treeview_w2v.insert("", "end", iid=i, text=files[i])

    def get_w2v_input(self):
        return self.in_box.get()

    def display_similarity(self, result):
        self.output_tree.delete(*self.output_tree.get_children())
        if type(result) is list:

            if len(result) is not None:
                for i, r in enumerate(result):
                    word = r[0]
                    cosine = r[1]
                    self.output_tree.insert("", "end", iid=i, text=word, values=cosine)
        else:
            self.output_tree.insert("", "end", iid=0, text="Word doesn't exist in vocab", values="N/A")

    def get_new_document(self) -> str:
        """
        Get the input from text box
        :return: The contents of the Text widget
        """
        return self.input_text.get("1.0", "end-1c")

    def display_topics(self, topics):
        self.treeview.delete(*self.treeview.get_children())

        for i, topic in enumerate(topics):
            self.treeview.insert("", "end", iid=i, text="Loaded documents", values=topic)

    def disable_add_directory(self):
        self.add_button['state'] = 'disabled'

    #def disable_add_dataset(self):
        # self.add_dataset['state'] = 'disabled'

    def disable_load_doc2vec(self):
        self.load_doc2vec['state'] = 'disabled'

    def enable_training_button(self):
        self.start_doc2vec['state'] = 'normal'

    def enable_classification_button(self, button_listener: InputController, param: int, ):
        self.start_classification['state'] = 'normal'

        if param == 0:
            self.start_classification.configure(command=button_listener.start_classification)
        else:
            self.start_classification.configure(command=button_listener.start_classification_loaded)

    def output_results(self, topics: list, results: np.array):
        results_gui = Doc2VecResultsGUI()
        results_gui.display_results(topics, results)
        results_gui.display()

    def display(self):
        """
        Display the window
        """
        self.root.mainloop()