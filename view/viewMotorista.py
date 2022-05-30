
from array import array
from tkinter import CENTER
import PySimpleGUI as sg

from model.motorista import Motorista
from view.view import View


class ViewMotorista(View):

    def __init__(self):
        super().__init__()

    def options(self, list: array):

        layout = [[sg.Button('Cadastrar motoristas', key='insert'), sg.Button('Pesquisar', key='search'), sg.Button('Motoristas excluídos', key='del_driver')],
                  [sg.Input(size=(20, 1), key='input')],
                  [sg.Listbox(list, expand_x=True,
                              expand_y=True, size=(50, 20), font=('Arial', 12),  pad=(20, 20), key='select')],
                  [sg.Button('Editar', key='edit')]
                  ]

        window = sg.Window('Motoristas', layout,
                           default_element_size=(12, 1), margins=(10, 10), element_justification=CENTER)

        while True:
            button, values = window.read()

            if button == 'search':
                new_values = []
                search = values['input']
                for object in list:
                    if search in object.nome.lower():
                        new_values.append(object)
                window['select'].update(new_values)
            else:
                break

        window.close()

        return button, values

    def display(self, motorista: Motorista = None):

        if motorista:

            layoutForm = [[sg.Text("Informações do motorista", font=('Arial', 14, 'bold'))],
                          [sg.Text('Nome', size=(15, 1)), sg.InputText(motorista.nome,
                                                                       key='nome')],
                          [sg.Text('CPF', size=(15, 1)), sg.InputText(motorista.cpf,
                                                                      key='cpf')],
                          [sg.Text('E-mail', size=(15, 1)),
                          sg.InputText(motorista.email, key='email')],
                          [sg.Text('Carga horária', size=(15, 1)),
                          sg.InputText(motorista.carga_horaria, key='carga_horaria')],
                          [sg.Text("Informações do veículo",
                                   font=('Arial', 14, 'bold'))],
                          [sg.Text('Tipo', size=(15, 1)), sg.InputText(motorista.veiculo.tipo,
                                                                       key='tipo')],
                          [sg.Text('Marca', size=(15, 1)), sg.InputText(motorista.veiculo.marca,
                                                                        key='marca')],
                          [sg.Text('Modelo', size=(15, 1)),
                          sg.InputText(motorista.veiculo.modelo, key='modelo')],
                          [sg.Text('Placa', size=(15, 1)), sg.InputText(
                              motorista.veiculo.placa, key='placa')],
                          [sg.Text('Capacidade', size=(15, 1)),
                          sg.InputText(motorista.veiculo.capacidade, key='capacidade')],
                          [sg.Text('Larg. Máx.', size=(15, 1)),
                          sg.InputText(motorista.veiculo.largura, key='largura')],
                          [sg.Text('Comp. Máx.', size=(15, 1)),
                          sg.InputText(motorista.veiculo.comprimento, key='comprimento')],
                          [sg.Text('Atura Máx.', size=(15, 1)),
                          sg.InputText(motorista.veiculo.altura, key='altura')]
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
        layout = [layoutForm, [sg.Button('Excluir', key='delete', disabled=True if not motorista else False), sg.Button(
            'Cancelar', key='cancel'), sg.Button('Cadastrar', key='save')]]

        window = sg.Window('Motoristas', layout,
                           default_element_size=(30, 1), margins=(50, 10), element_justification=CENTER)

        button, values = window.read()

        window.close()

        return button, values

    def del_driver(self, list: array):
        layout = [[sg.Button('Cadastrar motoristas', key='insert'), sg.Button('Pesquisar', key='search'), sg.Button('Motoristas excluídos', key='del_driver')],
                  [sg.Input(size=(20, 1), key='input')],
                  [sg.Listbox(list, expand_x=True,
                              expand_y=True, size=(50, 20), font=('Arial', 12),  pad=(20, 20), key='select')],
                  [sg.Button('Voltar', key='back')]
                  ]

        window = sg.Window('Motoristas', layout,
                           default_element_size=(12, 1), margins=(10, 10), element_justification=CENTER)

        while True:
            button, values = window.read()

            if button == 'search':
                new_values = []
                search = values['input']
                for object in list:
                    if search in object.nome.lower():
                        new_values.append(object)
                window['select'].update(new_values)
            else:
                break

        window.close()

        return button, values
