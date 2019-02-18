from tkinter import *
from tkinter.ttk import * #Treeview, Notebook, Style
from business_logic.controllers import InputController
from ui.Doc2VecResultsGUI import Doc2VecResultsGUI
import numpy as np


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
        self.root.title("Input GUI")
        self.root.geometry('700x600')
        self.root.resizable(False, False)

        # Class members
        self.add_button = None
        self.start_doc2vec = None
        self.start_classification = None
        self.confirm_dirs = None
        self.message = None
        self.treeview = None
        self.tab = None
        self.input_text = None
        self.add_doc = None
        self.classify_doc = None

        self.file_counter = 0
        # Operations
        self.root.lift()
        self.init_components()

    def init_components(self):
        """
        Initialise and output GUI widgets
        :return:
        """
        self.tab = Notebook(master=self.root)
        self.tab.pack(fill=BOTH, expand=1, padx=15, pady=15)

        doc2vec_frame = Frame()
        doc2vec_frame.pack()
        word2vec_frame = Frame()
        self.tab.add(doc2vec_frame, text="Doc2Vec")
        self.tab.add(word2vec_frame, text="Word2Vec")

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

        self.add_button = Button(master=button_frame, text="Add directory")
        self.add_button.pack(side=LEFT)
        self.start_doc2vec = Button(master=button_frame, state=DISABLED, text="Train Doc2Vec")
        self.start_doc2vec.pack(side=LEFT)
        self.start_classification = Button(master=button_frame, state=DISABLED, text="Train Classifier")
        self.start_classification.pack(side=LEFT)

        c_doc_frame = LabelFrame(master=doc2vec_frame, text="Document Classification")
        c_doc_frame.pack(fill=X, padx=15, pady=15)

        self.input_text = Text(master=c_doc_frame, height=3)
        self.input_text.pack(fill=X, padx=10, pady=10)

        self.add_doc = Button(master=c_doc_frame, text="Classify new document")
        self.add_doc.pack(side=LEFT, padx=10, pady=10)

    def set_button_commands(self, button_listener: InputController):
        """
        Attach button listeners to the button widgets of the window
        :param button_listener: The class that would handle button events.
        """
        self.add_button.configure(command=button_listener.add_directory)
        self.start_doc2vec.configure(command=button_listener.start_d2v)
        self.start_classification.configure(command=button_listener.start_classification)
        self.add_doc.configure(command=button_listener.process_new_document)

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

        for file in files:
            self.treeview.insert(self.file_counter, "end", text=file, values=topic)

    def get_new_document(self) -> str:
        """
        Get the input from text box
        :return: The contents of the Text widget
        """
        return self.input_text.get("1.0", "end-1c")

    def enable_training_button(self):
        self.start_doc2vec['state'] = 'normal'

    def enable_classification_button(self):
        self.start_classification['state'] = 'normal'

    def output_results(self, topics: list, results: np.array):
        results_gui = Doc2VecResultsGUI()
        results_gui.display_results(topics, results)
        results_gui.display()

    def display(self):
        """
        Display the window
        """
        self.root.mainloop()