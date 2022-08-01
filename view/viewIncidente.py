from array import array
from tkinter import BOTTOM, CENTER, TOP
from view.view import View
import PySimpleGUI as sg


class ViewIncidente(View):

    def __init__(self):
        super().__init__()

    def options(self):

        layout = [[sg.Text('Incidente', font=('Arial', 20, 'bold'))],
                  [self.text('Descrição'),
                           sg.Input(key='descricao', size=(30, 5))],
                  [self.text('Tipo'),
                           sg.Input(key='tipo', size=(30, 1))],
                  [self.button('Concluir', 'save', disableb=False)] 
                  ]

        window = self.window(layout)
        button, values = window.read()

        return button, values