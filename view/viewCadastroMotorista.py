
from array import array
from tkinter import CENTER
import PySimpleGUI as sg

from model.motorista import Motorista
from view.view import View


class ViewCadastroMotorista(View):

    def __init__(self):
        super().__init__()

    def options(self, list: array):

        layout = [[sg.Button('Cadastrar motoristas', key='insert', font=('Arial', 10, 'bold')), sg.Button('Pesquisar', key='search', font=('Arial', 10, 'bold')), sg.Button('Motoristas excluídos', key='del_driver', font=('Arial', 10, 'bold'))],
                  [sg.Input(size=(20, 5), key='input', expand_x=True)],
                  [self.list(list)],
                  [sg.Button('Editar', key='edit', font=(
                      'Arial', 10, 'bold'), size=(10, 1))]
                  ]

        window = self.window(layout)

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

            layoutForm = [[sg.Text("Informações do motorista", font=('Arial', 16, 'bold'))],
                          [self.text('Nome'), sg.Input(motorista.nome,
                                                       key='nome', size=(30, 1))],
                          [self.text('CPF'), sg.Input(motorista.cpf,
                                                      key='cpf', size=(30, 1))],
                          [self.text('E-mail'),
                          sg.Input(motorista.email, key='email', size=(30, 1))],
                          [self.text('Carga horária'),
                          sg.Input(motorista.carga_horaria, key='carga_horaria', size=(30, 1))],
                          [],
                          [sg.Text("Informações do veículo",
                                   font=('Arial', 14, 'bold'))],
                          [self.text('Tipo'), sg.Input(motorista.veiculo.tipo,
                                                       key='tipo', size=(30, 1))],
                          [self.text('Marca'), sg.Input(motorista.veiculo.marca,
                                                        key='marca', size=(30, 1))],
                          [self.text('Modelo'),
                          sg.Input(motorista.veiculo.modelo, key='modelo', size=(30, 1))],
                          [self.text('Placa'), sg.Input(
                              motorista.veiculo.placa, key='placa', size=(30, 1))],
                          [self.text('Capacidade'),
                          sg.Input(motorista.veiculo.capacidade, key='capacidade', size=(30, 1))],
                          [self.text('Larg. Máx.'),
                          sg.Input(motorista.veiculo.largura, key='largura', size=(30, 1))],
                          [self.text('Comp. Máx.'),
                          sg.Input(motorista.veiculo.comprimento, key='comprimento', size=(30, 1))],
                          [self.text('Altura Máx.'),
                          sg.Input(motorista.veiculo.altura, key='altura', size=(30, 1))]
                          ]

        else:
            layoutForm = [[sg.Text("Informações do motorista", font=('Arial', 16, 'bold'))],
                          [self.text('Nome'), sg.Input(
                              key='nome', size=(30, 1))],
                          [self.text('CPF'), sg.Input(
                              key='cpf', size=(30, 1))],
                          [self.text('E-mail'),
                          sg.In(key='email', size=(30, 1))],
                          [self.text('Carga horária'),
                          sg.Input(key='carga_horaria', size=(30, 1))],
                          [],
                          [sg.Text("Informações do veículo",
                                   font=('Arial', 16, 'bold'))],
                          [self.text('Tipo'), sg.Input(
                              key='tipo', size=(30, 1))],
                          [self.text('Marca'), sg.Input(
                              key='marca', size=(30, 1))],
                          [self.text('Modelo'),
                          sg.Input(key='modelo', size=(30, 1))],
                          [self.text('Placa'), sg.Input(
                              key='placa', size=(30, 1))],
                          [self.text('Capacidade'),
                          sg.Input(key='capacidade', size=(30, 1))],
                          [self.text('Larg. Máx.'),
                          sg.Input(key='largura', size=(30, 1))],
                          [self.text('Comp. Máx.'),
                          sg.Input(key='comprimento', size=(30, 1))],
                          [self.text('Altura Máx.'),
                          sg.Input(key='altura', size=(30, 1))]
                          ]
        layout = [[sg.Column(layoutForm)], [sg.Button('Excluir', key='delete', font=('Arial', 10, 'bold'), disabled=True if not motorista else False), sg.Button(
            'Cancelar', key='cancel', font=('Arial', 10, 'bold')), sg.Button('Cadastrar', key='save', font=('Arial', 10, 'bold'))]]

        window = self.window(layout)

        while True:
            button, values = window.read()

            if button == 'save':
                required = False

                for value in values:
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

    def del_driver(self, list: array):
        layout = [[sg.Button('Cadastrar motoristas', key='insert', font=('Arial', 10, 'bold')), sg.Button('Pesquisar', key='search', font=('Arial', 10, 'bold')), sg.Button('Motoristas excluídos', key='del_driver', font=('Arial', 10, 'bold'))],
                  [sg.Input(size=(20, 5), key='input', expand_x=True)],
                  [self.list(list)],
                  [sg.Button('Voltar', key='back', font=(
                      'Arial', 10, 'bold'), size=(10, 1))]
                  ]

        window = self.window(layout)

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
