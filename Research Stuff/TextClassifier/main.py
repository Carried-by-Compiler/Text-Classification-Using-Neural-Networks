from ui.InputGUI import InputGUI
from ui.Doc2VecResultsGUI import Doc2VecResultsGUI
from business_logic.controllers.InputController import InputController
from business_logic.readers.TxtReader import TxtReader
import numpy as np


if __name__ == "__main__":


    gui = InputGUI()
    controller = InputController(input_gui=gui, reader=TxtReader())
    """
    topics = ["tech", "politics", "literature", "tech", "politics", "literature", "tech", "politics", "literature", "tech", "politics", "literature", "tech", "politics", "literature", "tech", "politics", "literature"]
    results = np.array([0.32, 0.43, 0.53, 0.32, 0.43, 0.53, 0.32, 0.43, 0.53, 0.32, 0.43, 0.53, 0.32, 0.43, 0.53, 0.32, 0.43, 0.53])
    gui = Doc2VecResultsGUI()
    gui.display_results(topics, results)
    gui.display()
    """



