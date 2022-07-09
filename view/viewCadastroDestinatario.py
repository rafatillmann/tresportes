from array import array
from tkinter import CENTER
import PySimpleGUI as sg
from view.view import View
from model.destinatario import Destinatario


class ViewDestinatario(View):

    def __init__(self):
        super().__init__()

    def display(self, destinatario: Destinatario = None):

        if destinatario:

            layoutForm = [[sg.Text("Cadastro", font=('Arial', 14, 'bold'))],
                          [sg.Text('Nome', size=(15, 1)), sg.InputText(
                              destinatario.nome, key='nome')],
                          [sg.Text('CPF/CNPJ', size=(15, 1)), sg.InputText(
                              destinatario.cpf, key='cpf/cnpj')],
                          [sg.Text('Senha', size=(15, 1)),
                           sg.InputText(key='senha')],
                          [sg.Text('E-mail', size=(15, 1)),
                           sg.InputText(destinatario.email, key='email')],
                          [sg.Text('Endereço', size=(15, 1)), sg.InputText(
                              destinatario.endereco, key='endereco')],
                          [sg.Text('Complemento', size=(15, 1)), sg.InputText(
                              destinatario.complemento, key='complemento')],
                          [sg.Text('Telefone', size=(15, 1)), sg.InputText(
                              destinatario.telefone, key='telefone')],
                          ]

        else:
            layoutForm = [[sg.Text("Cadastro", font=('Arial', 14, 'bold'))],
                          [sg.Text('Nome', size=(15, 1)),
                           sg.InputText(key='nome')],
                          [sg.Text('CPF/CNPJ', size=(15, 1)),
                           sg.InputText(key='cpf/cnpj')],
                          [sg.Text('Senha', size=(15, 1)),
                           sg.InputText(key='senha')],
                          [sg.Text('E-mail', size=(15, 1)),
                           sg.InputText(key='email')],
                          [sg.Text('Endereço', size=(15, 1)),
                           sg.InputText(key='endereco')],
                          [sg.Text('Complemento', size=(15, 1)),
                           sg.InputText(key='complemento')],
                          [sg.Text('Telefone', size=(15, 1)),
                           sg.InputText(key='telefone')],
                          ]

        layout = [[sg.Column(layoutForm)], [
            sg.Button('Cadastrar', key='save')]]

        window = self.window(layout)

        while True:
            button, values = window.read()

            if button == 'save':
                required = False
                for value in values:
                    if destinatario:
                        if (values[value] == '' or values[value] == None) and value != 'senha':
                            required = True
                    else:
                        if values[value] == '' or values[value] == None:
                            required = True
                if required:
                    self.popUp(
                        'Obrigatório o preenchimento de todos os campos')
                else:
                    break
            else:
                break

        window.close()

        return button, values
