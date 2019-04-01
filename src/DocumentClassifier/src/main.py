from user_interfaces.main_gui import UserGUI
from business_logic.invoker import Invoker
from business_logic.commands.commands import *
from business_logic.managers.d2v_manager import D2VManager
from business_logic.managers.w2v_manager import W2VManager
from business_logic.readers.txt_reader import TxtReader
from business_logic.data_retriever import DataRetriever

if __name__ == "__main__":
    
    gui = UserGUI()
    retriever = DataRetriever(gui)
    d2v_manager = D2VManager(retriever)
    w2v_manager = W2VManager(retriever)

    d2v_manager.attach(gui)
    w2v_manager.attach(gui)

    # region Setting up invoker and commands
    invoker = Invoker()
    command1 = AddDirectoryCommand(d2v_manager)
    command2 = AddDatasetCommand(d2v_manager)
    command3 = LoadModelCommand(d2v_manager)
    command4 = TrainDoc2VecCommand(d2v_manager)
    command5 = TrainClassifierCommand(d2v_manager)
    command6 = ClassifyDocumentCommand(d2v_manager)
    command7 = AddFolderW2VCommand(w2v_manager)
    command8 = TrainWord2VecCommand(w2v_manager)
    command9 = GetSimilarWordsCommand(w2v_manager)
    invoker.store_command("ADD_DIR_D2V", command1)
    invoker.store_command("ADD_DATASET_D2V", command2)
    invoker.store_command("LOAD_D2V", command3)
    invoker.store_command("TRAIN_D2V", command4)
    invoker.store_command("TRAIN_CLASSIFIER", command5)
    invoker.store_command("CLASSIFY", command6)
    invoker.store_command("ADD_FOLDER", command7)
    invoker.store_command("TRAIN_W2V", command8)
    invoker.store_command("SIMILAR_WORDS", command9)
    # endregion

    gui.set_button_commands(invoker)
    gui.display()
