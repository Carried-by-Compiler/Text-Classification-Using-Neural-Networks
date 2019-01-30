from ui.InputGUI import InputGUI
from business_logic.controllers.InputController import InputController

if __name__ == "__main__":

    gui = InputGUI()
    controller = InputController(input_gui=gui, reader=None)

