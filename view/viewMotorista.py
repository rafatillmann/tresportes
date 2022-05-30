
from array import array
from tkinter import CENTER
import PySimpleGUI as sg

from model.motorista import Motorista
from view.view import View


class ViewMotorista(View):

    def __init__(self):
        super().__init__()

    def options(self, list: array):

        # motoristas = []

        # for i in list:
        #     motoristas.append(i.nome)

        layout = [[sg.Button('Cadastrar motoristas', key='insert'), sg.Button('Pesquisar'), sg.Button('Motoristas excluídos')],
                  [sg.Listbox(list, expand_x=True,
                              expand_y=True, size=(50, 20), font=('Arial', 12),  pad=(20, 20), key='select')],
                  [sg.Button('Editar', key='edit')]
                  ]

        window = sg.Window('Motoristas', layout,
                           default_element_size=(12, 1), margins=(10, 10), element_justification=CENTER)

        button, values = window.read()
        window.close()

        return button, values

    def display(self, motorista: Motorista = None):

        if motorista:

            layoutForm = [[sg.Text("Informações do motorista", font=('Arial', 14, 'bold'))],
                          [sg.Text('Nome', size=(15, 1)), sg.InputText(motorista.nome,
                                                                       key='nome')],
                          [sg.Text('CPF', size=(15, 1)), sg.InputText(
                              key='cpf')],
                          [sg.Text('E-mail', size=(15, 1)),
                           sg.In(key='email')],
                          [sg.Text('Carga horária', size=(15, 1)),
                           sg.InputText(key='carga_horaria')],
                          [sg.Text("Informações do veículo",
                                   font=('Arial', 14, 'bold'))],
                          [sg.Text('Tipo', size=(15, 1)), sg.InputText(
                              key='tipo')],
                          [sg.Text('Marca', size=(15, 1)), sg.InputText(
                              key='marca')],
                          [sg.Text('Modelo', size=(15, 1)),
                           sg.InputText(key='modelo')],
                          [sg.Text('Placa', size=(15, 1)), sg.InputText(
                              key='placa')],
                          [sg.Text('Capacidade', size=(15, 1)),
                           sg.InputText(key='capacidade')],
                          [sg.Text('Larg. Máx.', size=(15, 1)),
                           sg.InputText(key='largura')],
                          [sg.Text('Comp. Máx.', size=(15, 1)),
                           sg.InputText(key='comprimento')],
                          [sg.Text('Atura Máx.', size=(15, 1)),
                           sg.InputText(key='altura')]
                          ]

        else:
            layoutForm = [[sg.Text("Informações do motorista", font=('Arial', 14, 'bold'))],
                          [sg.Text('Nome', size=(15, 1)), sg.InputText(
                              key='nome')],
                          [sg.Text('CPF', size=(15, 1)), sg.InputText(
                              key='cpf')],
                          [sg.Text('E-mail', size=(15, 1)),
                           sg.In(key='email')],
                          [sg.Text('Carga horária', size=(15, 1)),
                           sg.InputText(key='carga_horaria')],
                          [sg.Text("Informações do veículo",
                                   font=('Arial', 14, 'bold'))],
                          [sg.Text('Tipo', size=(15, 1)), sg.InputText(
                              key='tipo')],
                          [sg.Text('Marca', size=(15, 1)), sg.InputText(
                              key='marca')],
                          [sg.Text('Modelo', size=(15, 1)),
                           sg.InputText(key='modelo')],
                          [sg.Text('Placa', size=(15, 1)), sg.InputText(
                              key='placa')],
                          [sg.Text('Capacidade', size=(15, 1)),
                           sg.InputText(key='capacidade')],
                          [sg.Text('Larg. Máx.', size=(15, 1)),
                           sg.InputText(key='largura')],
                          [sg.Text('Comp. Máx.', size=(15, 1)),
                           sg.InputText(key='comprimento')],
                          [sg.Text('Atura Máx.', size=(15, 1)),
                           sg.InputText(key='altura')]
                          ]
        layout = [layoutForm, [sg.Button('Excluir', key='delete'), sg.Button(
            'Cancelar', key='cancel'), sg.Button('Cadastrar', key='save')]]

        window = sg.Window('Motoristas', layout,
                           default_element_size=(30, 1), margins=(10, 10), size=(500, 500), element_justification=CENTER)

        button, values = window.read()
        window.close()

        return button, values

    def update(self):
        pass
