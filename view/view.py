from abc import ABC, abstractmethod
import PySimpleGUI as sg


class View(ABC):

    def __init__(self):
        self.theme()

    def theme(self):
        theme = {"BACKGROUND": "#F3F3F3",
                 "TEXT": "#222624",
                 "INPUT": "#D9D9D9",
                 "TEXT_INPUT": "#222624",
                 "SCROLL": "#222624",
                 "BUTTON": ("#FFFFFF", "#222624"),
                 "PROGRESS": ("#222624", "#222624"),
                 "BORDER": 1,
                 "SLIDER_DEPTH": 0,
                 "PROGRESS_DEPTH": 0}
        sg.theme_add_new("Tresportes", theme)
        sg.theme("Tresportes")
        sg.set_options(element_padding=(8, 8))
