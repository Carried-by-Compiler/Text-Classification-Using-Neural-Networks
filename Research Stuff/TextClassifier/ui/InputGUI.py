from tkinter import *
from tkinter.ttk import Treeview
from business_logic.controllers.InputController import InputController


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
        #self.root.geometry('500x500')

        # Class members
        self.controller = None

        self.greet_button = None
        self.close_button = None
        self.add_button = None
        self.message = None
        self.treeview = None

        # Operations
        self.init_components()

    def init_components(self):

        # Top Frame
        top_frame = Frame(master=self.root, background="blue")
        top_frame.pack(fill=X, padx=15, pady=20)

        m = "Please provide the file path to the directories containing the training documents. " \
            "The name of the directory will be the TOPIC/SUBJECT associated with the documents " \
            "contained within that directory."
        self.message = Message(master=top_frame, text=m, relief="raised")
        self.message.bind("<Configure>", lambda event: event.widget.configure(width=event.width - 8))
        self.message.pack(fill=X)

        # Middle Frame
        middle_frame = Frame(master=self.root)
        middle_frame.pack(fill=X, padx=15)

        # Construct the tree view
        # https://stackoverflow.com/questions/22456445/how-to-imitate-this-table-using-tkinter
        self.treeview = Treeview(master=middle_frame)
        self.treeview['columns'] = "topic"
        self.treeview.heading("#0", text="File Path")
        self.treeview.column("#0", anchor="center")
        self.treeview.heading("topic", text="Topic/Subject")
        self.treeview.column("topic", anchor="center")

        self.treeview.pack(fill=X, side=LEFT)

        vsb = Scrollbar(master=middle_frame, orient="vertical", command=self.treeview.yview)
        vsb.pack(side="right", fill=Y)
        self.treeview.configure(yscrollcommand=vsb.set)

        self.add_button = Button(master=self.root, text="Add directory")
        self.add_button.pack(pady=10, side=BOTTOM)

    def set_button_commands(self, button_listener: InputController):
        self.add_button.configure(command=button_listener.add_directory)

    def add_new_directory(self, path: str, topic: str):
        self.treeview.insert("", "end", text=path, values=topic)

    def greet(self):
        print("Greetings!")

    def display(self):
        self.root.mainloop()