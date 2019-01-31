from tkinter import *
from tkinter.ttk import * #Treeview, Notebook, Style
from business_logic.controllers import InputController


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
        self.root.geometry('700x500')

        # Class members
        self.add_button = None
        self.start_doc2vec = None
        self.confirm_dirs = None
        self.message = None
        self.treeview = None
        self.tab = None

        self.file_counter = 0
        # Operations
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

        bottom_frame = Frame(master=training_frame)
        bottom_frame.pack(padx=10, pady=10, fill=X, expand=0)

        self.add_button = Button(master=bottom_frame, text="Add directory")
        self.add_button.pack(side=LEFT)
        self.confirm_dirs = Button(master=bottom_frame, text="Load documents")
        self.confirm_dirs.pack(side=LEFT, padx=5)
        self.start_doc2vec = Button(master=bottom_frame, state=DISABLED, text="Train Doc2Vec")
        self.start_doc2vec.pack(side=LEFT)

    def set_button_commands(self, button_listener: InputController):
        """
        Attach button listeners to the button widgets of the window
        :param button_listener: The class that would handle button events.
        """
        self.add_button.configure(command=button_listener.add_directory)
        self.confirm_dirs.configure(command=button_listener.confirm_selection)
        self.start_doc2vec.configure(command=button_listener.start_d2v)

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

    def enable_training_button(self):
        self.start_doc2vec['state'] = 'normal'

    def display(self):
        """
        Display the window
        """
        self.root.mainloop()