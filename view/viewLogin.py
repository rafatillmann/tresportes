import PySimpleGUI as sg

from view.view import View


class ViewLogin(View):

    def __init__(self):
        super().__init__()

    def login(self):
        layout = [
            [sg.Text('Login', font=(25))],
            [sg.Text('Email', size=(15, 1)),
             sg.InputText(key='email')],
            [sg.Text('Senha', size=(15, 1)),
             sg.InputText(key='password')],
            [sg.Submit('OK'), sg.Cancel('Cancelar', key='cancel')]
        ]

        window = sg.Window('Login').Layout(layout)
        button, values = window.Read()

        window.close()

        if button == 'OK':
            return values['email'], values['password']
        else:
            return False
