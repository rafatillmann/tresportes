from tkinter import CENTER
import PySimpleGUI as sg

from view.view import View


class ViewLogin(View):

    def __init__(self):
        super().__init__()

    def login(self):
        layout = [
            [sg.Image(source='./assets/login.png')],
            [sg.Text('Login', font=('Arial', 25, 'bold'), p=15)],
            [sg.Text('Email', size=(10, 1), font=('Arial', 11, 'bold')),
             sg.InputText(key='email', size=(25, 1))],
            [sg.Text('Senha', size=(10, 1), font=('Arial', 11, 'bold')),
             sg.InputText(key='senha', size=(25, 1))],
            [sg.Submit('OK', key='save', font=('Arial', 10, 'bold')), sg.Cancel(
                'Cancelar', key='cancel', font=('Arial', 10, 'bold')), sg.Button('Cadastrar', key='insert', font=('Arial', 10, 'bold'))]
        ]

        window = sg.Window('Trêsportes', layout,
                           default_element_size=(30, 1), margins=(50, 10), element_justification=CENTER, resizable=True)
        button, values = window.read()

        window.close()

        return button, values
