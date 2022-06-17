from abc import ABC, abstractmethod
import PySimpleGUI as sg
from tkinter import CENTER, RIGHT, TOP


class View(ABC):

    @abstractmethod
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
                 "PROGRESS_DEPTH": 0, }
        sg.theme_add_new("Tresportes", theme)
        sg.theme("Tresportes")
        sg.set_options(element_padding=(10, 10))

    def popUp(self, msg: str = 'Um problema inesperado ocorreu, tente novamente!'):
        sg.popup(msg, title='Trêsportes')

    def window(self, layout):
        screen = [
            [sg.Column(self.menu(), vertical_alignment=TOP, background_color="#222624", element_justification=CENTER, pad=0, expand_y=True), sg.Column(layout, pad=(20, 20))]]
        return sg.Window('Trêsportes', screen,
                         default_element_size=(12, 1), margins=(0, 0), resizable=True)

    def menu(self):
        menu = [[sg.Image(source='./assets/route.png', background_color="#222624", )],
                [sg.Button(button_text='Rotas', key='route', size=(
                    15, 2), font=('Arial', 10, 'bold'), pad=0, border_width=0)],
                [sg.Image(source='./assets/driver.png',
                          background_color="#222624", )],
                [sg.Button('Motoristas', key='driver', size=(
                    15, 2), font=('Arial', 10, 'bold'), pad=0, border_width=0)],
                [sg.Image(source='./assets/load.png',
                          background_color="#222624", )],
                [sg.Button('Cargas', key='load', size=(
                    15, 2), font=('Arial', 10, 'bold'), pad=0, border_width=0)],
                ]
        return menu

    def text(self, text):
        return sg.Text(text, size=(15, 1), font=('Arial', 10, 'bold'))

    def list(self, list):
        return sg.Listbox(list, expand_x=True, font=(12),
                          expand_y=True, size=(None, 20), key='select')
