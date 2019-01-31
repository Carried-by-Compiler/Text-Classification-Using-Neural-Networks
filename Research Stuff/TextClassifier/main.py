from ui.InputGUI import InputGUI
from business_logic.controllers.InputController import InputController
from business_logic.readers.TxtReader import TxtReader


if __name__ == "__main__":

    gui = InputGUI()
    controller = InputController(input_gui=gui, reader=TxtReader())

